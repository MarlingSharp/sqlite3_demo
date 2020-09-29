from common import select_data

SQL_GET_STUDENTS = "SELECT id, name, age FROM student; "

if __name__ == "__main__":
    rows = select_data(SQL_GET_STUDENTS)
    for row in rows:
        print(row)
