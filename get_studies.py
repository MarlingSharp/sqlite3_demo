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

if __name__ == "__main__":
    student_id = request_id('student')
    rows = select_data(SQL_GET_STUDIES, str(student_id)) # Student ID needs to be a string??!
    for row in rows:
        print(row)
