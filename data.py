import sys

f = open("Data.csv", "r")
analyse = sys.argv[1]

cost = 0
paid = 0
balance = 0
clientList = []
#next(f)

for line in f:
	try:
		entry = line.strip("\n").split(",")
		
		if analyse == "all":
			cost += int(entry[2])
			paid += int(entry[3])
			balance += int(entry[4])
		elif entry[5] == analyse:
			cost += int(entry[2])
			paid += int(entry[3])
			balance += int(entry[4])
			clientList.append(entry[1])
	except:
		pass

if analyse != "all":
	print "\n" + str(len(clientList)) + " client(s) are " + analyse + ":"
	for client in clientList:
		print client
	
print "\nTotals for " + analyse + " entries:"
print "Cost: " + str(cost)
print "Paid: " + str(paid)
print "Balance: " + str(balance)

f.close()