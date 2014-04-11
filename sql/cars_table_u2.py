# Create a SQLite3 database and table


# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect("cars.db") as connection:
	c=connection.cursor()

	c = connection.cursor()
	c.execute("UPDATE inventory SET quantity = 20 WHERE Model='Focus'")
	c.execute("UPDATE inventory SET quantity=10 WHERE Make='Ford' AND Model='Taurus'")

	rows=c.execute("SELECT * FROM inventory")
	for r in rows:
		if r[0]=='Ford':
			print r[0],r[1],r[2]