from connect import * # import the connect module

def deleteGame(id):
  if id == None:
    cursor.execute(f"DELETE FROM Games")
    conn.commit
    print("All records have been deleted! ")
  else:
    # Select word for printing before deletion
    cursor.execute(f"SELECT game_name FROM Games WHERE game_id = {id} ")
    game = str(cursor.fetchone()).translate({ord(i): None for i in "(',)"})

    #delete word by ID
    cursor.execute(f"DELETE FROM Games WHERE game_id = {id}")
    conn.commit()
    
    print(f"\n'{game}' deleted from the games table")