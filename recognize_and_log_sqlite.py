import face_recognition
import cv2
import numpy as np
import pickle
import sqlite3
from datetime import datetime

# ---------- DATABASE CONNECTION ----------
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# ---------- LOAD ENCODINGS ----------
with open("encodings/encodings.pickle", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

print("[INFO] Starting webcam for real-time recognition... Press 'q' to exit.")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect and encode faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        name = "Unknown"
        if matches[best_match_index]:
            name = known_names[best_match_index]

            # Check if attendance already marked today
            today_date = datetime.now().strftime("%Y-%m-%d")
            cursor.execute("SELECT * FROM attendance WHERE name=? AND date=?", (name, today_date))
            result = cursor.fetchall()

            if not result:
                current_time = datetime.now().strftime("%H:%M:%S")
                cursor.execute("INSERT INTO attendance (name, date, time) VALUES (?, ?, ?)",
                               (name, today_date, current_time))
                conn.commit()
                print(f"[INFO] Attendance marked for {name} at {current_time}")

        # Draw rectangle and name on webcam
        top, right, bottom, left = [v*4 for v in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Smart Attendance System (SQLite)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
conn.close()
