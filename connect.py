import sqlite3 as sql

"""Create a connection object that represent the database you want to create and/or use in order to 
use the SQLite module imported in step 1"""

conn = sql.connect("gameData.db")

"""create a cursor object after establishing a connection
in step 2, and call its execute() method to perform SQL commands  """

cursor = conn.cursor()