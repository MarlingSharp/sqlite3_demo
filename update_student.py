from common import request_id, execute_sql

SQL_UPDATE = "UPDATE student SET name=?, age=? WHERE id=?;"

def update_student():
  # Ask the user for the required details
  the_id = request_id('student')
  the_name = input('Enter new name: ')
  the_age = int(input('Enter new age: '))

  # Create a tuple with the values to insert
  updates = (the_name, the_age, the_id)
  execute_sql(SQL_UPDATE, updates)

if __name__ == "__main__":
  update_student()