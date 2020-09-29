from create_database import create_database
from delete_database import delete_database
from get_students import get_students
from get_studies import get_studies
from get_subjects import get_subjects
from insert_student import insert_student
from insert_studies import insert_studies
from insert_subject import insert_subject
from delete_student import delete_student
from common import run_any_select, run_any_execute

db_functions = [
  ('Create Database', create_database),
  ('Delete Database', delete_database),
  ('Get Students', get_students),
  ('Get Studies', get_studies),
  ('Get Subjects', get_subjects),
  ('Insert Student', insert_student),
  ('Insert Studies', insert_studies),
  ('Insert Subject', insert_subject),
  ('Insert Subject', insert_subject),
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