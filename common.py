import sqlite3
from sqlite3 import Error
"""
With thanks to 
https://www.sqlitetutorial.net/sqlite-python/create-tables/
"""

DB_FILENAME = 'mydb.db'

def select_data(sql, criteria=()):
  conn = None
  try:
      conn = sqlite3.connect(DB_FILENAME)
      print(f"Connected to SQLite3 version {sqlite3.version}")

      cur = conn.cursor()

      print(f"Retrieving Data with {sql}")
      cur.execute(sql, criteria)

      return cur.fetchall()
  except Error as e:
      print(e)
  finally:
      if conn:
          conn.close()


def execute_sql(sql, data=()):
    conn = None
    try:
        conn = sqlite3.connect(DB_FILENAME)
        print(f"Connected to SQLite3 version {sqlite3.version}")

        cur = conn.cursor()

        print(f"Executing {sql} with {data}")
        cur.execute(sql, data)
        conn.commit()

        print(f"Amended Row with ID {cur.lastrowid}")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def request_id(table_name, primary_key='id', secondary_key='name'):
    rows = select_data(f"SELECT {primary_key}, {secondary_key} FROM {table_name}")
    print(f'Here is the data from {table_name}')
    print('ID\tName')
    valid_ids = []
    for r in rows:
        print(f"{r[0]}\t{r[1]}")
        valid_ids.append(r[0])

    while True:
        try:
            selected_id = int(input(f"Select an ID from {table_name}: "))

            if selected_id not in valid_ids:
                raise ValueError('Invalid ID')
            else:
                return selected_id
        except ValueError:
            print('Invalid ID, try again...')

def run_any_select():
  print('Type your SQL command and press Enter')
  sql = input()
  rows = select_data(sql)
  for r in rows:
    print(r)

def run_any_execute():
  print('Type your SQL command and press Enter')
  sql = input()
  execute_sql(sql)