from common import request_id, execute_sql

SQL_UPDATE = "UPDATE subject SET name=?, teacher=? WHERE id=?;"

def update_subject():
  # Ask the user for the required details
  the_id = request_id('subject')
  the_name = input('Enter new name: ')
  the_teacher = input('Enter new teacher: ')

  # Create a tuple with the values to insert
  updates = (the_name, the_teacher, the_id)
  execute_sql(SQL_UPDATE, updates)

if __name__ == "__main__":
  update_subject()