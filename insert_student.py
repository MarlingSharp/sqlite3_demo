from common import insert_data

SQL_INSERT_STUDENT = "INSERT INTO student (name, age) VALUES (?, ?);"

if __name__ == "__main__":

    # Ask the user for the required details
    student_name = input('Enter new student name: ')
    student_age = int(input('Enter new student age: '))

    # Create a tuple with the values to insert
    new_student = (student_name, student_age)
    insert_data(SQL_INSERT_STUDENT, new_student)