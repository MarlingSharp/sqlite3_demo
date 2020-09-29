from common import insert_data

SQL_INSERT_SUBJECT = "INSERT INTO subject (name, teacher) VALUES (?, ?);"

if __name__ == "__main__":

    # Ask the user for the required details
    subject_name = input('Enter new subject name: ')
    subject_teacher = input(f'Enter teacher of {subject_name}: ')

    # Create a tuple with the values to insert
    new_subject = (subject_name, subject_teacher)
    insert_data(SQL_INSERT_SUBJECT, new_subject)
