import sys

f = open("Data.csv", "r")
analyse = sys.argv[1]

cost = 0
paid = 0
balance = 0

analyse_cost = 0
analyse_paid = 0
analyse_balance = 0
clientList = []
#next(f)

for line in f:
	try:
		entry = line.strip("\n").split(",")
		
		cost += int(entry[2])
		paid += int(entry[3])
		balance += int(entry[4])
		
		if entry[5] == analyse:
			analyse_cost += int(entry[2])
			analyse_paid += int(entry[3])
			analyse_balance += int(entry[4])
			clientList.append(entry[1])
	except:
		pass

print "\nGrand totals:"
print "Cost: " + str(cost)
print "Paid: " + str(paid)
print "Balance: " + str(balance)
		
print "\n" + str(len(clientList)) + " client(s) are " + analyse + ":"
for client in clientList:
	print client

if len(clientList) > 0:		
	print "\nTotals for " + analyse + " entries:"
	print "Cost: " + str(analyse_cost)
	print "Paid: " + str(analyse_paid)
	print "Balance: " + str(analyse_balance)

f.close()