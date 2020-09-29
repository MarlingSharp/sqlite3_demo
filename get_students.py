from common import select_data

SQL_GET_STUDENTS = "SELECT id, name, age FROM student; "

def get_students():
  rows = select_data(SQL_GET_STUDENTS)
  for row in rows:
      print(row)

if __name__ == "__main__":
  rows = get_students()
  for row in rows:
    print(row)
