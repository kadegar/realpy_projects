# Create a SQLite3 database and table


# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect("cars.db") as connection:
	c=connection.cursor()

	currinv= [
		('Ford','Focus',3),
		('Ford','Taurus',2),
		('Honda','Accord',5),
		('Porsche','911',1),
		('Lambourghini','convertible',1)
		]
	c.executemany('INSERT INTO inventory VALUES(?,?,?)', currinv)
	