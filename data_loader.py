import sys
import MySQLdb

#Connect to mySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="fh3h9f444yKbeo433", db="sales")
#Create cursor object to allow you to execute queries
cur = db.cursor()

cur.execute("SELECT * FROM info")
for row in cur.fetchall():
	print row

f = open("Data.csv", "r")

for line in f:
	entry = line.strip("\n").split(",")
	print entry
	
f.close()