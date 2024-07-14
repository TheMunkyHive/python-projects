''' 
Python SQLite Tutorial

Workflow:   Create database -> Create table -> (methods) INSERT, UPDATE, DELETE, SELECT, DROP 
            -> commit -> close

Datatypes:  NULL, INTEGER, TEXT, REAL, BLOB
            BLOB = (Binary large objects) Storage of binary data
            SQLite3 doesnt have BOOLEAN Datatype -> INT TRUE=1, FALSE=0

Database cursor: Pointer to the database object to handle modifications

Table Columns: Column "ROWID" is an ID column with autoincrement which sqlite adds to every table

Column datatype constraints: NOT NULL, UNIQUE, DEFAULT, PRIMARY KEY, FOREIGN KEY

'''

# SQLite Database connection  skeleton

# Import module
import sqlite3

# Connect to the database
def dbConnect():
    try:
        db = sqlite3.connect("sqlite-tutorial.db")
        # Create Database Object Pointer 
        cursor = db.cursor()
        print("Connected to database!")
        return db, cursor
    except Exception as e:
        print(f"ERROR: f(dbConnect) {e}")
        exit(1)

# Close connection to the database
def dbClose():
    try:
        db.close()
        print("Closed database connection!")
        return db
    except Exception as e:
        print(f"ERROR: f(dbClose) {e}")
        exit(1)

# Create Table

def dbCreateTable():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers(
                   first_name TEXT,
                   last_name TEXT,
                   age INTEGER,
                   email TEXT,
                   active INTEGER
        ) 
        ''')

        # Commit changes to the database
        db.commit()
    except Exception as e:
        print(f"ERROR: f(dbCreateTable) {e}")


db, cursor = dbConnect()
dbCreateTable()

# print(f"DEBUG:  DB = {db}, CURSOR = {cursor}")
dbClose()
