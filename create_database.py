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
                                    teacher integer NOT NULL
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

SQL_CREATE_BASIC_DATA = [
    "INSERT INTO student (id, name, age) VALUES (1, 'Harry', 14)",
    "INSERT INTO student (id, name, age) VALUES (2, 'Ron', 15)",
    "INSERT INTO student (id, name, age) VALUES (3, 'Hermione', 15)",
    "INSERT INTO student (id, name, age) VALUES (4, 'Draco', 14)",
    "INSERT INTO subject (id, name, teacher) VALUES (1, 'Potions', 'Severus Snape')",
    "INSERT INTO subject (id, name, teacher) VALUES (2, 'Transfiguration', 'Minerva McGonagall')",
    "INSERT INTO subject (id, name, teacher) VALUES (3, 'Charms', 'Prof Flitwick')",
    "INSERT INTO subject (id, name, teacher) VALUES (4, 'Care of Magical Creatues', 'Rubeus Hagrid')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (1, 1, 'E')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (1, 2, 'D')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (1, 3, 'O')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (2, 1, 'E')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (2, 3, 'D')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (2, 4, 'P')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (3, 1, 'E')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (3, 2, 'O')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (3, 3, 'O')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (3, 4, 'O')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (4, 2, 'E')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (4, 3, 'O')",
    "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (4, 4, 'P')"
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

        for t in SQL_CREATE_BASIC_DATA:
            print(t)
            cur.execute(t)
        conn.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_database()