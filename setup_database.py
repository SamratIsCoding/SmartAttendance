import sqlite3

# Connect to SQLite (creates file if it doesn't exist)
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Create attendance table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    time TEXT
)
""")

conn.commit()
conn.close()

print("✅ SQLite database and attendance table are ready!")
