import sqlite3

conn=sqlite3.connect("new.db")

cursor=conn.cursor()

try:
	cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
	cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")
except sqlite3.OperationalError:
	print sqlite3.OperationalError
	print "Opps! You screwed up."
	raise