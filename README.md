# Smart Attendance System using Face Recognition

## 📌 Project Overview
The **Smart Attendance System using Face Recognition** is an AI-driven application that automates attendance marking in educational and workplace settings.  
Using Python, OpenCV, and SQLite, the system:

- Detects and recognizes faces in real-time through a webcam  
- Logs attendance with **name, date, and timestamp**  
- Exports attendance reports to **Excel/CSV**  
- Eliminates manual roll-call and reduces human error

---

## 🚀 Features
- ✅ Real-time face detection & recognition  
- ✅ Automatic attendance logging in **SQLite database**  
- ✅ One-time attendance marking per day  
- ✅ Console-based attendance reporting  
- ✅ Export attendance to **Excel or CSV**  
- ✅ Lightweight, no external DB server required

---

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries:** 
  - OpenCV  
  - face_recognition  
  - numpy  
  - pandas & openpyxl (for reporting)  
- **Database:** SQLite3 (built-in with Python)

---

## 📂 Project Structure
```bash
SmartAttendance/
│
├── dataset/ # Captured face images for each user
├── encodings/ # Face encodings (encodings.pickle)
│
├── attendance.db # SQLite database storing attendance
├── report.xlsx # Sample exported report
│
├── capture_faces.py # Capture face images
├── encode_faces.py # Generate and save face encodings
├── recognize_and_log_sqlite.py # Real-time recognition & attendance logging
├── attendance_report.py # Reporting and export tool
├── setup_database.py # Initializes SQLite DB & table
└── README.md # Project Documentation
```


---

## ⚡ Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/SmartAttendance.git
   cd SmartAttendance
2. **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    venv\Scripts\activate   # On Windows
    source venv/bin/activate  # On Linux/Mac
3. **Install Required Dependencies**
    ```bash
    pip install opencv-python face_recognition numpy pandas openpyxl
4. **Setup the Database**
    ```bash
    python setup_database.py

## ▶️ How to Run the Project

**Step 1: Capture Faces**
```bash
python capture_faces.py
```
 - Captures face images and stores them in dataset/username/.

**Step 2: Generate Face Encodings**
```bash
python encode_faces.py
```
 - Converts face images into encodings and stores in encodings/encodings.pickle.

**Step 3: Start Attendance System**
```bash
python attendance_report.py
```
 - Starts webcam for real-time recognition
 - Press q to exit

**Step 4: Reporting and Export**
```bash
python attendance_report.py
```
 - View all records or export to Excel/CSV

## 🔮 Future Scope
- GUI Dashboard for easy management
- Real-time notifications (Email/WhatsApp)
- Liveness detection to avoid spoofing
- Cloud-based storage and analytics
- Multi-camera and multi-location support

## 📜 License
This project is developed for academic and demonstration purposes.
You may modify and use it for learning or institutional projects.