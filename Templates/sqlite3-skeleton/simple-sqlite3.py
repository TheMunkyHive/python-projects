import sqlite3

def dbConnect():
	try:
		db = sqlite3.connect("/tmp/test.db")
	except Exception as e:
		print("ERROR: ", e)
		exit()
	
	db.close()

dbConnect()

