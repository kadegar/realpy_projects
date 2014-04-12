import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	makes_models=c.execute("SELECT make,model,COUNT(*) from orders group by make,model")
	for m in makes_models:
			print m
