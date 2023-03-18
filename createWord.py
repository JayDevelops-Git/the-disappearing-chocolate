from connect import *
from time import sleep
from datetime import datetime
# import readWords
import string
alphabet = list(string.ascii_lowercase)

def addWord(word):
    validWord = False

    while validWord == False:

        if len(word) < 3:
            word = input("\nPlease enter a word with a minimum length of 3: ")

        elif len(word) > 20:
            word = input("\n Your word has exceeded the maximum character length of 20. Please enter a shorter word: ")

        # Checks to see if word contains characters only fromn the alphabet (removes all spaces before checking)
        elif word.replace(' ','').isalpha() == False:
            word = input("\nPlease enter a valid word (letters and spaces only): ")

        # TODO: check if word is already in 'words' database
        # cursor.execute("SELECT Word FROM ")
        else:
            validWord = True
       

    wordEntry=[]

    word = " ".join(word.split()).lower()
    date = datetime.today().strftime('%d-%m-%Y')

    wordEntry.append(word)
    wordEntry.append(date)

    cursor.execute("INSERT INTO Words VALUES(NULL, ?, ?)", wordEntry)
    conn.commit()
    print(f"'{word}' added to the words list")
    sleep(3)

    """
    cursor.execute("SELECT * FROM Words") # select all words
    # Fetchall() method, fetches all rows from the last executed statement
    row = cursor.fetchall()
    for record in row:
        print(record)
    """
