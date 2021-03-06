import sqlite3
from sqlite3 import Error

from common import DB_FILENAME

SQL_INSERT_STUDENT = "INSERT INTO student (id, name, age) VALUES (?, ?, ?)"
SQL_INSERT_SUBJECT = "INSERT INTO subject (id, name, teacher) VALUES (?, ?, ?)"
SQL_INSERT_STUDIES = "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (?, ?, ?)"

def insert_from_csv(cur, sql, csv_file):
  csv_file = open(csv_file, 'r')
  csv_lines = csv_file.readlines() 

  for csv_line in csv_lines:
    parts = csv_line.strip().split(',')
    print(parts)
    cur.execute(sql, parts)

def populate_database():
    conn = None
    csv_file = None
    try:
        conn = sqlite3.connect(DB_FILENAME)
        print(f"Connected to SQLite3 version {sqlite3.version}")

        cur = conn.cursor()
        insert_from_csv(cur, SQL_INSERT_STUDENT, 'students.csv')
        insert_from_csv(cur, SQL_INSERT_SUBJECT, 'subjects.csv')
        insert_from_csv(cur, SQL_INSERT_STUDIES, 'studies.csv')
        
        conn.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        if csv_file:
            csv_file.close()

if __name__ == "__main__":
    populate_database()