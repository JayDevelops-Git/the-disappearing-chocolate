from playMenu import playMenu
from recordsMenu import recordsMenu
from time import sleep
from wordBankMenu import wordBankMenu
from sys import exit
import os.path
from createTbls import createTbls

menu = """"
    --------------------------
    THE DISAPPEARING CHOCOLATE
    --------------------------
    Welcome to the Disappearing Chocolate - a Hangman alternative.

    Please select an option from the menu below:

    1. Quick Play
    2. Past Games
    3. Word Bank
    4. Exit
    """

menuChoices = [
  "1", "one", "quick play", "2", "two", "3", "three", "past games", "4", "four", "word bank", "exit"
]


def mainMenu():

  while os.path.isfile('gameData.db') != True:
    try:
      createTbls()
    except FileExistsError:
      print("DB File Exists Already!")

  validSelection = False
  exitMenu = False

  print(menu)

  # Program will continue to run indefinitely unless user chooses to exit at this point
  while exitMenu == False:
    # Checks if correct menu option selected
    while validSelection == False:
      menuChoice = input(str("Your selection: ")).lower()
      if menuChoice in menuChoices:
        validSelection = True
      else:
        print("Please enter a valid option. \n")

    if menuChoice == "1" or menuChoice == "one" or menuChoice == "quick play":
      playMenu()

    elif menuChoice == "2" or menuChoice == "two" or menuChoice == "past games":
      recordsMenu()

    elif menuChoice == "3" or menuChoice == "three" or menuChoice == "word bank":
      wordBankMenu()

    elif menuChoice == "4" or menuChoice == "four" or menuChoice == "exit":
      print("Thank you for playing!")
      exitMenu = True
      exit()

    else:
      sleep(1.5)
      mainMenu()

    # Reset if user exits sub-menus
    menuChoice = None


mainMenu()
