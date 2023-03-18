from readGames import read
from time import sleep
from deleteGame import deleteGame

menu = """
    --------------------
        RECORDS MENU
    --------------------
    Please select an option from the menu below:

    1. View
    2. Delete
    3. Delete All
    4. Back
    """

menuChoices = ["1", "one", "view", "2", "two", "delete", "3", "three", "delete all", "4", "four", "back"]

def recordsMenu():
    validSelection = False
    
    print(menu)

    # Checks if correct menu option selected
    while validSelection == False:
        menuChoice = input(str("Your selection: ")).lower()
        if menuChoice in menuChoices:
            validSelection = True
        else:
            print(menu)
            print("Please enter a valid option. \n")
    
    # Option 1 - View
    if menuChoice == menuChoices[0] or menuChoice == menuChoices[1] or menuChoice == menuChoices[2]:
        read()
        sleep(1.5)
        recordsMenu()
    
    # Option 2 - Delete
    elif menuChoice == menuChoices[3] or menuChoice == menuChoices[4] or menuChoice == menuChoices[5]:
        read()
        sleep(1.5)
        id = int(input("Enter the ID of the game you wish to delete: "))
        deleteGame(id)

    # Option 3 - Delete All
    elif menuChoice == menuChoices[6] or menuChoice == menuChoices[7] or menuChoice == menuChoices[8]:
        deleteGame(None)

    # Option 4 - Back
    elif menuChoice == menuChoices[9] or menuChoice == menuChoices[10] or menuChoice == menuChoices[11]:
        return