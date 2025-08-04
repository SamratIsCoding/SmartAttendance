import sqlite3
import pandas as pd

DB_PATH = "attendance.db"

def fetch_all_attendance():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM attendance ORDER BY date, time", conn)
    conn.close()
    return df

def fetch_attendance_by_date(date_str):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM attendance WHERE date=? ORDER BY time", conn, params=(date_str,))
    conn.close()
    return df

def export_to_excel(df, filename):
    df.to_excel(filename, index=False)
    print(f"✅ Attendance exported to {filename}")

if __name__ == "__main__":
    print("Attendance Reporting Tool")
    print("1. View All Records")
    print("2. View by Date")
    print("3. Export to Excel")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        df = fetch_all_attendance()
        print(df if not df.empty else "No attendance records found.")

    elif choice == "2":
        date_str = input("Enter date (YYYY-MM-DD): ")
        df = fetch_attendance_by_date(date_str)
        print(df if not df.empty else f"No records found for {date_str}.")

    elif choice == "3":
        df = fetch_all_attendance()
        if df.empty:
            print("No data to export!")
        else:
            filename = input("Enter export filename (e.g., report.xlsx): ")
            export_to_excel(df, filename)

    else:
        print("❌ Invalid choice!")
