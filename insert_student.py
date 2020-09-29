import sqlite3
from sqlite3 import Error

from common import DB_FILENAME

conn = None
try:
    conn = sqlite3.connect(DB_FILENAME)
    print(f"Connected to SQLite3 version {sqlite3.version}")

    cur = conn.cursor()

    student_name = input('Enter new student name: ')
    student_age = int(input('Enter new student age: '))
    sql_insert_student = "INSERT INTO student (name, age) VALUES (?, ?);"

    # Create a tuple with the values to insert
    new_student = (student_name, student_age)

    print("Inserting Student")
    cur.execute(sql_insert_student, new_student)
    conn.commit()

    print(f"Student created with ID {cur.lastrowid}")
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()
