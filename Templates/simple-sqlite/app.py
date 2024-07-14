import sqlite3

try:
    conn = sqlite3.connect("database.sqlite")
    c = conn.cursor()
    print("Connected to the database!")
except Exception as e:
    print(f"Error: {e}")

# Using 'with' you can ommit conn.commit() at the end of the operation
# which conn:
#   c.execute("INSERT INTO test VALUES (:name)", {'name': link})

def insertData(link):
    c.execute("INSERT INTO test VALUES (:name)", {'name': link})
    print(f"Inserting URL: {link}")
    conn.commit()

# Delete all entries from a table: c.execute("DELETE FROM test")
# deleteData(), deletes all rows from the table sequentially
def deleteData(rows):
    for x in range(1, rows+1):
        # c.execute(f"DELETE FROM test WHERE ROWID={x}")
        c.execute("DELETE FROM test WHERE ROWID = :id", {'id': x})
        print(f"Deleting ROW: {x}")
        conn.commit()

def showData():
    c.execute("SELECT ROWID,* FROM test")

    query = c.fetchall()
    rows = query[-1][0]

    for id, URL in query:
        print(f"ID = {id}, Name: {URL}")

    return rows

rows = showData()
deleteData(rows)
insertData("http://linuxpool.de")

conn.close()
