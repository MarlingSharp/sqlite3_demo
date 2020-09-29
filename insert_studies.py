from common import insert_data, request_id

SQL_INSERT_STUDY = "INSERT INTO studies (student_id, subject_id) VALUES (?, ?);"


if __name__ == "__main__":

    # Ask the user for the required details
    student_id = request_id('student')
    subject_id = request_id('subject')

    # Create a tuple with the values to insert
    new_study = (student_id, subject_id)
    insert_data(SQL_INSERT_STUDY, new_study)
