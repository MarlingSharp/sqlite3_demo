from common import select_data

SQL_GET_SUBJECTS = "SELECT id, name, teacher FROM subject; "

def get_subjects():
  rows = select_data(SQL_GET_SUBJECTS)
  for row in rows:
    print(row)

if __name__ == "__main__":
  get_subjects()

