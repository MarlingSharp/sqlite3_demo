from common import select_data, request_id

SQL_GET_STUDIES = """
    SELECT student.name, subject.name FROM student
    INNER JOIN studies ON
        student.id = studies.student_id
    INNER JOIN subject ON
        studies.subject_id = subject.id
    WHERE student.id = ?
    ; 
"""

def get_studies():
  student_id = request_id('student')

  # Student ID needs to be a string??!
  rows = select_data(SQL_GET_STUDIES, str(student_id))

  for row in rows:
    print(row) 


if __name__ == "__main__":
  get_studies()
    
    
