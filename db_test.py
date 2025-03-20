import MySQLdb

db = MySQLdb.connect(
	host = "localhost",
	user = "root",
	password = "password",
	db = "test_db"
)

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print("Database version:", data)

db.close