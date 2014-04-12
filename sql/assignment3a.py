import sqlite3, random

with sqlite3.connect("newnum.db") as connection:

	cursor=connection.cursor()

	cursor.execute("DROP TABLE if exists numbers")
	cursor.execute("""CREATE TABLE numbers
		(numbers INT)
		""")
	for i in range(100):
		cursor.execute("INSERT INTO numbers(numbers) VALUES(?)",(random.randint(0,100),))

