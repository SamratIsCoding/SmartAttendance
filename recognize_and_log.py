import face_recognition
import cv2
import numpy as np
import pickle
import os
import pandas as pd
from datetime import datetime

# Load the known face encodings
with open("encodings/encodings.pickle", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

# Create attendance folder
os.makedirs("attendance", exist_ok=True)

# Prepare today's CSV file
today = datetime.now().strftime("%Y-%m-%d")
csv_path = f"attendance/attendance_{today}.csv"

# If file doesn't exist, create it with headers
if not os.path.exists(csv_path):
    df = pd.DataFrame(columns=["Name", "Date", "Time"])
    df.to_csv(csv_path, index=False)

print("[INFO] Starting webcam for real-time recognition... Press 'q' to exit.")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Find all face locations and encodings in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        name = "Unknown"
        if matches[best_match_index]:
            name = known_names[best_match_index]

            # Read current attendance
            df = pd.read_csv(csv_path)
            today_date = datetime.now().strftime("%Y-%m-%d")

            # Check if already marked today
            if not ((df['Name'] == name) & (df['Date'] == today_date)).any():
                current_time = datetime.now().strftime("%H:%M:%S")
                new_entry = pd.DataFrame([[name, today_date, current_time]], columns=["Name", "Date", "Time"])
                df = pd.concat([df, new_entry], ignore_index=True)
                df.to_csv(csv_path, index=False)
                print(f"[INFO] Attendance marked for {name} at {current_time}")

        # Display face name on webcam
        top, right, bottom, left = [v*4 for v in face_location]  # scale back to original size
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Smart Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
