import face_recognition
import pickle
import os
import cv2

# Paths
dataset_path = "dataset"
encodings_path = "encodings/encodings.pickle"

known_encodings = []
known_names = []

print("[INFO] Encoding faces...")

# Loop through each person in the dataset
for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)
    
    if not os.path.isdir(person_folder):
        continue

    # Loop through each image of the person
    for img_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_name)
        image = cv2.imread(img_path)
        
        # Convert image from BGR (OpenCV) to RGB (face_recognition uses RGB)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detect face locations
        boxes = face_recognition.face_locations(rgb, model='hog')  # 'cnn' is slower but more accurate
        encodings = face_recognition.face_encodings(rgb, boxes)

        # Store each encoding with its name
        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)

# Save encodings to file
os.makedirs("encodings", exist_ok=True)
data = {"encodings": known_encodings, "names": known_names}

with open(encodings_path, "wb") as f:
    pickle.dump(data, f)

print(f"[INFO] Encodings saved to {encodings_path}")
print(f"[INFO] Total encoded faces: {len(known_encodings)}")
