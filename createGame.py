from connect import *
from time import sleep
from datetime import datetime
import readGames
import string
alphabet = list(string.ascii_lowercase)

def createGame(playerId, gameName, guessList, gameWon):
    gameEntry=[]

    lettersGuessed = len(guessList)
    date = datetime.today().strftime('%d-%m-%Y')

    gameEntry.append(playerId)
    gameEntry.append(gameName)
    gameEntry.append(lettersGuessed)
    gameEntry.append(gameWon)
    gameEntry.append(date)

    cursor.execute("INSERT INTO Games VALUES(NULL, ?, ?, NULL, ?, ?, ?)", gameEntry)
    conn.commit()
    print(f"Game: '{gameName}' recorded!")
    sleep(3)
