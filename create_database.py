import sqlite3
from sqlite3 import Error

from common import DB_FILENAME

sql_create_student_table = """ CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    age integer NOT NULL
                            ); """

"""
With thanks to 
https://www.sqlitetutorial.net/sqlite-python/create-tables/
"""
if __name__ == '__main__':
    conn = None
    try:
        conn = sqlite3.connect(DB_FILENAME)
        print(f"Connected to SQLite3 version {sqlite3.version}")

        cur = conn.cursor()

        print("Creating Student Table")
        cur.execute(sql_create_student_table)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()