from connect import *

def read():
    cursor.execute("SELECT * FROM games") # select all games
    # Fetchall() method, fetches all rows from the last executed statement
    row = cursor.fetchall()
    for record in row:
        print(record)


# if this file is run directly as a main file run the code first
# otherwise if this file (readRecords.py) is invoked in another file (as a child)
#do not automatically run it
if __name__ == "__main__":
    read()