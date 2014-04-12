import sqlite3

print "Do you want AVG, MAX, MIN, OR SUM?"
x=raw_input()

with sqlite3.connect("newnum.db") as connection:

	cursor=connection.cursor()

	if x=="AVG":
		result=cursor.execute("SELECT AVG(numbers) from numbers")
		for r in result:
			print r[0]
	elif x=="MAX":
		result=cursor.execute("SELECT MAX(numbers) from numbers")
		for r in result:
			print r[0]
	elif x=="MIN":
		result=cursor.execute("SELECT MIN(numbers) from numbers")
		for r in result:
			print r[0]
	elif x=="SUM":
		result=cursor.execute("SELECT SUM(numbers) from numbers")
		for r in result:
			print r[0]
	else:
		print "I'm sorry, that's not a valid input"
