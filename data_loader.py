import sys
import MySQLdb

#Connect to mySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="fh3h9f444yKbeo433", db="sales")
#Create cursor object to allow you to execute queries
cur = db.cursor()

f = open("Data.csv", "r")
next(f)

for line in f:
	entry = line.strip("\n").split(",")
	query = "INSERT INTO transaction(date, name, cost, paid, balance, status) VALUES ('" + entry[0] + "', '" + entry[1] + "', '" + entry[2] + "', '" + entry[3] + "', '" + entry[4] + "', '" + entry[5] + "')"
	cur.execute(query)

db.commit()
f.close()