import sys

f = open("Data.csv", "r")

balance = 0
next(f)
for line in f:
	entry = line.strip("\n").split(",")
	balance += int(entry[4])

print "Balance: " + str(balance)

f.close()