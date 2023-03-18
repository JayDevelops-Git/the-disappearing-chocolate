import string
from time import sleep
from readWords import getRandomWord
from createGame import createGame


fullBar = """
      ___  ___  ___  ___  ___.---------------.
.'\__\'\__\'\__\'\__\'\__,`   .  ____ ___ \
|\/ __\/ __\/ __\/ __\/ _:\   |`.  \  \___ \
 \\'\__\'\__\'\__\'\__\'\_`.__|""`. \  \___ \
  \\/ __\/ __\/ __\/ __\/ __:                \
   \\'\__\'\__\'\__\ \__\'\_;-----------------`
    \\/   \/   \/   \/   \/ :                 |
     \|______________________;________________|
    """
word =""
numberOfGuesses = 7
incorrectGuesses = 0
# A tuple of triples (word letter, TRUE/FALSE), true if has been guessed, false if not
wordList = []

#Used in checkGuess()
guessList = []
alphabet = list(string.ascii_uppercase)
alphabetRemaining = alphabet
alphabetReset = False

def playMenu():
    play()
    wordGuessed = False
    while wordGuessed != True and (numberOfGuesses-incorrectGuesses != 0):
        showStatement()
        guess = input(str("\n\nMake a guess: ")).upper().strip()
        if guess.lower() == "quit":
            return None
        wordGuessed = checkGuess(guess)
      
    if wordGuessed == True:
        showStatement()
        print(f"\nYou successfully guessed the word with {numberOfGuesses-incorrectGuesses} bites of chocolate left!\n")
        gameName = str(input("Please enter a name for this game: "))
        createGame(None,gameName,guessList,wordGuessed)
    else:
        showStatement()
        print(f"\nThe chocolate has been eaten!\nThe word was {word}.\n")
        gameName = str(input("Please enter a name for this game: "))
        createGame(None,gameName,guessList,wordGuessed)
    

# Identifies if a guess is valid and updates the user accordingly
# Returns true if word has been sucessfully guessed
def checkGuess(letter):
    global wordList
    global alphabetRemaining
    if letter == word.upper():
        # Updates each pair in wordList to true, therefore revealing the letters
        for i in word:
            update(i)
        return True
        
    elif len(letter) > 1:
        print("\nYou can only guess one letter or the whole word. Try again.")
        return False

    elif letter not in alphabet:
        print("\nYour guess is not a valid letter. Try again.")
        return False

    elif letter in guessList:
        print("\nLetter already guessed. Try again.")
        return False
    
    # If guess is valid (single alphabet letter, not already guessed),
    # returns true if all letters guessed and false if still unguessed letters
    else:
        guessList.append(letter)
        guessList.sort()
        alphabetRemaining = [x for x in alphabet if x not in guessList]
        
        return update(letter)

# Updates wordList, changing tuple for a specific letter to true, revealing the hidden letter when printed
# Checks list to see if all letters have been guessed - if so returns true
def update(letter):
    global wordList
    global incorrectGuesses
    correctGuess = False
    letter = letter.lower()
    for pos, tup in enumerate(wordList):
        if tup[0] == letter:
            wordList[pos] = (letter,True)
            correctGuess = True

    isTrue = 0
    for pos, tup in enumerate(wordList):
        if tup[1] == True:
            isTrue = isTrue +1
    
    if correctGuess != True:
        incorrectGuesses += 1
    if isTrue == len(word):
        return True
    else: 
        return False

# Resets global variables, initialises the word to be guessed
def play():
    global guessList
    guessList = []

    global incorrectGuesses
    incorrectGuesses = 0

    global word
    word = getRandomWord()

    global wordList
    wordList = createWordList()

    global alphabetRemaining
    alphabetRemaining = alphabet

# Prints underscores for letters not guessed and displays the correctly guessed letters
def showStatement():
    sleep(1)
    print("\n\n-------------------------\n-------------------------\n\n Your word is below:")
    # print(wordList)
    for tup in wordList:
        if tup[1] == False:
            print("_", end=" ")
        else:
            print(tup[0], end=" ")
    
    print("\n\nBites of chocolate left: ", numberOfGuesses-incorrectGuesses)
    print(f"\nLetters guessed: "+ ', '.join(guessList))
    print(f"Letters available: "+ '  '.join(alphabetRemaining))
    sleep(1)


# Turns letters in word to '_' for guessing. Also resets the global variables for every game.
def createWordList():
    global wordList
    wordList = []
    
    # Creates a tuple of pairs (letter, TRUE/FALSE), true if has been guessed, false if not. Initally all false
    for i in word:
        if (i == " "):
            wordList.append(tuple(["  ", True]))
        else:
            wordList.append(tuple([i, False])) 
    return wordList
