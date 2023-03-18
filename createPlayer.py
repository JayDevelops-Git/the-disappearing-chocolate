from connect import *
from time import sleep
import readRecords

def createPlayer():
    players=[]

    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    username = input("Enter Username: ")
    # PlayerID is auto increment and does not require user input

    players.append(firstName)
    players.append(lastName)
    players.append(username)
    #print(players)

    # insert data into players table

    #INSERT INTO players (firstName lastName, username) VALUES(Bad,MJ,Pop) # firstName,lastName,username
    #INSERT INTO players VALUES(NULL,Bad,MJ,Pop) #firstName,lastName,username
    cursor.execute("INSERT INTO players VALUES(NULL, ?, ?, ?)", players)
    conn.commit()
    print(f"Player {firstName} '{username}' {lastName} added to players table")
    sleep(3)

    cursor.execute("SELECT * FROM players") # select all players
    # Fetchall() method, fetches all rows from the last executed statement
    row = cursor.fetchall()
    for record in row:
        print(record)

createPlayer()