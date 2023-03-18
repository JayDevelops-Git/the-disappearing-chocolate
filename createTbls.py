from connect import *

def createTbls():
	cursor.execute(
		""" 
	CREATE TABLE "Players" (
		"player_id"	INTEGER NOT NULL UNIQUE,
		"first_name"	TEXT,
		"last_name"	TEXT,
		"username"	TEXT,
		PRIMARY KEY("player_id" AUTOINCREMENT)
	)"""
	)
	# ...........................
	cursor.execute(
		"""
	CREATE TABLE "Words" (
		"word_id"	INTEGER NOT NULL UNIQUE,
		"word"	TEXT,
		"date_created"	TEXT,
		PRIMARY KEY("word_id" AUTOINCREMENT)
	)"""
	)
	# ...............................
	cursor.execute(
		"""
	CREATE TABLE "Games" (
		"game_id"	INTEGER NOT NULL UNIQUE,
		"player_id"	INTEGER,
		"game_name"	TEXT,
		"word_id"	INTEGER,
		"letters_guessed"	INTEGER,
		"game_won"   BOOLEAN,
		"date"    TEXT,
		PRIMARY KEY("game_id" AUTOINCREMENT)
		FOREIGN KEY("player_id") REFERENCES "players"("player_id")
		FOREIGN KEY("word_id") REFERENCES "words"("word_id")
	)"""
	)