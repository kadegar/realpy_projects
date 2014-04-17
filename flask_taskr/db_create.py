# db_create.py

import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	c=connection.cursor()
	c.execute("""CREATE TABLE ftasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)""")

	c.execute('INSERT INTO ftasks(name,due_date,priority,status) VALUES("Learn Python","6/30/14",10,1)')
	c.execute('INSERT INTO ftasks(name,due_date,priority,status) VALUES("Finish this tutorial","5/1/14",8,1)')