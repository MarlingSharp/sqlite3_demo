from common import execute_sql, request_id

SQL_INSERT_STUDY = "INSERT INTO studies (student_id, subject_id, target_grade) VALUES (?, ?, ?);"

def insert_studies():
  # Ask the user for the required details
  student_id = request_id('student')
  subject_id = request_id('subject')
  target_grade = input('Enter target grade: ')

  # Create a tuple with the values to insert
  new_study = (student_id, subject_id, target_grade)
  execute_sql(SQL_INSERT_STUDY, new_study)

if __name__ == "__main__":
  insert_studies()
    