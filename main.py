from create_database import create_database
from populate_database import populate_database
from delete_database import delete_database
from get_students import get_students
from insert_student import insert_student
from delete_student import delete_student
from common import run_any_select, run_any_execute

db_functions = [
  ('Create Database', create_database),
  ('Populate Database', populate_database),
  ('Delete Database', delete_database),
  ('Get Students', get_students),
  ('Insert Student', insert_student),
  ('Delete Student', delete_student),
  ('Run SELECT SQL', run_any_select),
  ('Run INSERT/UPDATE/DELETE SQL', run_any_execute),
]

EXIT_CODE = 'x'

print('Welcome to Database Manager')

while True:
  # Print the menu
  print('-----Menu------')
  for num, (name, func) in enumerate(db_functions):
    print(f'{num}: {name}')
  print(f'{EXIT_CODE}: Exit')

  try:
    user = input('Make a selection: ')
    if user == EXIT_CODE:
      break

    # otherwise parse as numerical
    user = int(user)
    if user < len(db_functions):
      db_functions[user][1]()

      print('Press Enter to return to Menu')
      input()
    else:
      raise ValueError('Invalid selection')
  except ValueError as e:
    print(e)

print('Done')