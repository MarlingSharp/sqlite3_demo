import sqlite3
from sqlite3 import Error

from common import DB_FILENAME

SQL_CREATE_STUDENT_TABLE = """ CREATE TABLE student (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    age integer NOT NULL
                            ); """

def create_database():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILENAME)
        print(f"Connected to SQLite3 version {sqlite3.version}")

        cur = conn.cursor()

        print(SQL_CREATE_STUDENT_TABLE)
        cur.execute(SQL_CREATE_STUDENT_TABLE)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_database()