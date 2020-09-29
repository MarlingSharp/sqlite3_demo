import sqlite3
from sqlite3 import Error

from common import DB_FILENAME

conn = None
try:
    conn = sqlite3.connect(DB_FILENAME)
    print(f"Connected to SQLite3 version {sqlite3.version}")

    cur = conn.cursor()

    sql_get_students = "SELECT name, age FROM student; "

    print("Retrieving Students")
    cur.execute(sql_get_students)

    rows = cur.fetchall()

    for row in rows:
        print(row)
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()
