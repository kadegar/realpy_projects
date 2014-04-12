import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	
	sql={'average': "SELECT avg(population) FROM population",
		'minimum':"SELECT min(population) FROM population",
		'maximum': "SELECT max(population) FROM population",
		'sum': "SELECT sum(population) FROM population",
		'count':"SELECT count(population) FROM population"}

	for keys,values in sql.iteritems():
		c.execute(values)

		result=c.fetchone()
		print keys+": ", result[0]
		