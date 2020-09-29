import os

from common import DB_FILENAME

def delete_database():
  os.remove(DB_FILENAME)