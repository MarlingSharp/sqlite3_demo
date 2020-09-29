from common import execute_sql, request_id

SQL_DELETE_STUDIES = """
  DELETE FROM studies WHERE student_id = ?
"""

SQL_DELETE_STUDENT = """
  DELETE FROM student WHERE id=?
"""

def delete_student():
  student_id = request_id('student')
  d = (str(student_id))

  # Clean up studies first
  execute_sql(SQL_DELETE_STUDIES, d)
  execute_sql(SQL_DELETE_STUDENT, d)