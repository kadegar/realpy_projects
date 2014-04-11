import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
	c=connection.cursor()
	employees=csv.reader(open("employees.csv","rU"))
	c.execute("CREATE TABLE employees(NAME, JOB_TITLE, DEPARTMENT, EMPLOYEE_ANNUAL_SALARY, ESTIMATED_ANNUAL_SALARY)")
	c.executemany("INSERT INTO employees(NAME, JOB_TITLE, DEPARTMENT, EMPLOYEE_ANNUAL_SALARY, ESTIMATED_ANNUAL_SALARY) values (?, ?, ?, ?, ?)",
employees)