from connect import * # import the connect module

def deleteWord(id):
  if id == None:
    cursor.execute(f"DELETE FROM Words")
    conn.commit
    print("The word bank has been reset! ")
  else:
    # Select word for printing before deletion
    cursor.execute(f"SELECT word FROM Words WHERE word_id = {id} ")
    word = str(cursor.fetchone()).translate({ord(i): None for i in "(',)"})

    #delete word by ID
    cursor.execute(f"DELETE FROM Words WHERE word_id = {id}")
    conn.commit()
    
    print(f"\n'{word}' deleted from the words table")