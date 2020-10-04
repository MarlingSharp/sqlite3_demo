from common import execute_sql, request_id

SQL_DELETE_STUDIES = """
  DELETE FROM studies WHERE subject_id = ?
"""

SQL_DELETE_SUBJECT = """
  DELETE FROM subject WHERE id=?
"""

def delete_subject():
  subject_id = request_id('subject')
  d = (subject_id,)

  # Clean up 'studies' first
  execute_sql(SQL_DELETE_STUDIES, d)

  # Now we can safely delete the student
  execute_sql(SQL_DELETE_SUBJECT, d)