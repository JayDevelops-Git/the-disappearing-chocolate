from time import sleep
from readWords import read
from createWord import addWord
from deleteWord import deleteWord


menu = """
    --------------------
         WORD BANK
    --------------------
    Please select an option from the menu below:

    1. View
    2. Add
    3. Remove
    4. Back
    """

deleteMenu = """
    --------------------
        DELETE MENU
    --------------------
    Please select an option from the menu below:

    1. Delete
    2. Delete All
    3. Back
    """

menuChoices = ["1", "one", "view", "2", "two", "add", "3", "three", "delete", "4", "four", "back"]

def wordBankMenu():
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

    
    # Option 1 - View Words
    if menuChoice == menuChoices[0] or menuChoice == menuChoices[1] or menuChoice == menuChoices[2]:
        read()
        sleep(1.5)
        wordBankMenu()
    
    # Option 2 - Add Words
    elif menuChoice == menuChoices[3] or menuChoice == menuChoices[4] or menuChoice == menuChoices[5]:
        addingWords = True
        read()
        sleep(1.5)
        while addingWords == True:
            addWord(input("Enter the word you wish to add: "))
            again = input("Would you like to add another word? (Y/N): ").lower()
            if again == "y" or again == "yes":
                addingWords = True
            else:
                addingWords = False
                sleep(1.5)
                wordBankMenu()
                
    # Option 3 - Remove Words
    elif menuChoice == menuChoices[6] or menuChoice == menuChoices[7] or menuChoice == menuChoices[8]:
        print(deleteMenu)
        sleep(1.5)
        deleteOption = input("\nSelect an option: ").lower()
        # Delete one word
        if deleteOption == "1" or deleteOption == "one" or deleteOption == "delete":
            deletingWords = True
            while deletingWords ==True:
                read()
                sleep(1.5)
                deleteWord(int(input("\nEnter the ID of the word you wish to delete: ")))
                again = input("\nWould you like to delete another word? (Y/N): ").lower()
                if again == "y" or again == "yes":
                    deletingWords = True
                else:
                    deletingWords = False
                    sleep(1.5)
                    wordBankMenu()
        # Delete all words
        elif deleteOption == "2" or deleteOption == "two" or deleteOption == "delete all":
            deleteWord(None)
        else:
            sleep(1.5)
            wordBankMenu()
    
    # Option 4 - Back to main menu
    elif menuChoice == menuChoices[9] or menuChoice == menuChoices[10] or menuChoice == menuChoices[11]:
        return
