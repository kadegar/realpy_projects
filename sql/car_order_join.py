import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)""")

# (again, copy and paste the values if you'd like)
	ordr = [
	('Ford', 'Taurus', '2013-11-12'),
	('Honda', 'Accord', '2013-12-01'),
	('Ford', 'Taurus', '2013-04-23'),
	('Honda', 'Accord', '2013-12-09'),
	('Porsche', '911', '2013-05-29'),
	('Honda', 'Accord', '2013-12-11'),
	('Ford', 'Focus', '2014-01-12'),
	('Ford', 'Focus', '2014-03-16'),
	('Lambourghini', 'convertible', '2013-10-10'),
	('Honda', 'Accord', '2013-04-21'),
	('Ford', 'Taurus', '2013-06-12'),
	('Ford', 'Focus', '2013-08-19'),
	('Ford', 'Taurus', '2013-08-22'),
	('Honda', 'Accord', '2013-12-23'),
	]

	c.executemany("INSERT INTO orders VALUES(?, ? ,? )", ordr)
	
	c.execute("""SELECT DISTINCT inventory.make,inventory.model,inventory.quantity,orders.order_date FROM inventory,orders WHERE inventory.make=orders.make AND inventory.model=orders.model ORDER BY orders.order_date ASC""")
	rows=c.fetchall()
	for r in rows:
		print "Make: "+r[0]
		print "Model: " +r[1]
		print "Inventory: "+str(r[2])
		print "Order date: "+str(r[3]) 
