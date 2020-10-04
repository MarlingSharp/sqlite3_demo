import sqlite3
from sqlite3 import Error

from common import DB_FILENAME

SQL_CREATE_STUDENT_TABLE = """ CREATE TABLE student (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    age integer NOT NULL
                            ); """
SQL_CREATE_SUBJECT_TABLE = """ CREATE TABLE subject (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    teacher text NOT NULL
                            ); """
SQL_CREATE_STUDIES_TABLE = """ CREATE TABLE studies (
                                student_id integer,
                                subject_id integer,
                                target_grade text NOT NULL,
                                CONSTRAINT studies_pk PRIMARY KEY (student_id, subject_id),
                                CONSTRAINT FK_student FOREIGN KEY (student_id) REFERENCES student (id),
                                CONSTRAINT FK_subject FOREIGN KEY (subject_id) REFERENCES subject (id)
                            ); """

SQL_CREATE_TABLES = [
    SQL_CREATE_STUDENT_TABLE,
    SQL_CREATE_SUBJECT_TABLE,
    SQL_CREATE_STUDIES_TABLE
]

def create_database():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILENAME)
        print(f"Connected to SQLite3 version {sqlite3.version}")

        cur = conn.cursor()

        for t in SQL_CREATE_TABLES:
            print(t)
            cur.execute(t)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_database()