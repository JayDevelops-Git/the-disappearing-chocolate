from connect import *
from random import randrange

wordList = []

def read():
    cursor.execute("SELECT * FROM Games") # select all words
    # Fetchall() method, fetches all rows from the last executed statement
    row = cursor.fetchall()
    print("\n --- Recorded Games ---\n")
    print("\n\nGame ID / Player ID / Game Name / Word ID / Letters Guessed / Game Won / Date\n")
    for record in row:
        print(record)
    print("\n")

# if this file is run directly as a main file run the code first
# otherwise if this file (readRecords.py) is invoked in another file (as a child)
#do not automatically run it
if __name__ == "__main__":
    read()
