from connect import *
from time import sleep
from readRecords import read

def update():
    #use gameID (unique key) to update records in songs table
    idfield = input("Enter the ID of the game you want to update: ")
    fieldName = input("Which field would you like to update? (Name / Word/ Guesses / Successful): ")

    newFieldValue = input(f"Enter the value for the {fieldName}")
    print(newFieldValue)
    newFieldValue="'" + newFieldValue +"'"
    print(newFieldValue)

    #UPDATE songs SET itle/Artist/Genre = TitleVal/ArtistVal/GenreVal WHERE SongID = 1/2/3/4/5...
    cursor.execute(f"UPDATE songs SET {fieldName} = {newFieldValue} WHERE SongID = {idfield}")
    conn.commit()

    print(f"Record {idfield} updated in the song table")
    sleep(3)

    read()

update()
