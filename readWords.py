from connect import *
from random import randrange

wordList = []

def read():
    cursor.execute("SELECT * FROM Words") # select all words
    # Fetchall() method, fetches all rows from the last executed statement
    row = cursor.fetchall()
    print("\n --- Current words ---\n")
    for record in row:
        print(record)
    print("\n")

def getRandomWord():
    setWordList()
    global wordList
    # Adding default word list here to prevent any issues of having no words to guess
    wordList = wordList + getDefaultWords()
    return wordList[randrange(len(wordList))]

def getDefaultWords():
    defaultWords = ["apple", "beach", "caterpillar", "driveway"]
    return defaultWords

def setWordList(): 
    global wordList
    wordList = []
    cursor.execute("SELECT word FROM Words")
    row = cursor.fetchall()
    for record in row:
        word = str(record).translate({ord(i): None for i in "(',)"})
        wordList.append(word)
    # print(wordList)

# if this file is run directly as a main file run the code first
# otherwise if this file (readRecords.py) is invoked in another file (as a child)
#do not automatically run it
if __name__ == "__main__":
    read()
