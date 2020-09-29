from common import select_data

SQL_GET_SUBJECTS = "SELECT id, name, teacher FROM subject; "

if __name__ == "__main__":
    rows = select_data(SQL_GET_SUBJECTS)
    for row in rows:
        print(row)

