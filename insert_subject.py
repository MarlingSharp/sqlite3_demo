from common import execute_sql

SQL_INSERT_SUBJECT = "INSERT INTO subject (name, teacher) VALUES (?, ?);"

def insert_subject():
  # Ask the user for the required details
  subject_name = input('Enter new subject name: ')
  subject_teacher = input(f'Enter teacher of {subject_name}: ')

  # Create a tuple with the values to insert
  new_subject = (subject_name, subject_teacher)
  execute_sql(SQL_INSERT_SUBJECT, new_subject)

if __name__ == "__main__":
  insert_subject()
    
