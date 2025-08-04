import cv2
import os

# Ask for the user's name
person_name = input("Enter the name of the person: ").strip()

# Path to save images
dataset_path = "dataset"
person_folder = os.path.join(dataset_path, person_name)

# Create folder if it doesn't exist
os.makedirs(person_folder, exist_ok=True)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Load Haarcascade for face detection (comes with OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

print("[INFO] Capturing faces. Press 'q' to quit...")

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Save face region as image
        face_img = frame[y:y+h, x:x+w]
        img_path = os.path.join(person_folder, f"{count}.jpg")
        cv2.imwrite(img_path, face_img)
        count += 1

    cv2.imshow("Capturing Faces", frame)

    # Break if 'q' is pressed or 50 images captured
    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
        break

print(f"[INFO] Captured {count} images for {person_name}")

cap.release()
cv2.destroyAllWindows()
