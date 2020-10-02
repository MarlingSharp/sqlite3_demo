from common import execute_sql, request_id

SQL_DELETE_STUDENT = """
  DELETE FROM student WHERE id=?
"""

def delete_student():
  student_id = request_id('student')
  d = (student_id,)

  # Now we can safely delete the student
  execute_sql(SQL_DELETE_STUDENT, d)