def calcAnalysis(record):
	#cost, paid, balance
	return [int(record[2]), int(record[3]), int(record[4])]

### MAIN PROGRAM ###
import sys

f = open("Data.csv", "r")
analyse = sys.argv[1]

cost = 0
paid = 0
balance = 0

#closed, open, pending -- cost, paid, balance
analysis = [[0,0,0],[0,0,0],[0,0,0]]
clientList = [[],[],[]]
#next(f)

for line in f:
	try:
		entry = line.strip("\n").split(",")
		
		cost += int(entry[2])
		paid += int(entry[3])
		balance += int(entry[4])
		
		if int(entry[4])==0:
			analysis[0] = [sum(x) for x in zip(analysis[0], calcAnalysis(entry))]
			clientList[0].append(entry[1])			
		elif int(entry[3])==0:
			analysis[2] = [sum(x) for x in zip(analysis[2], calcAnalysis(entry))]
			clientList[2].append(entry[1])			
		else:
			analysis[1] = [sum(x) for x in zip(analysis[1], calcAnalysis(entry))]
			clientList[1].append(entry[1])			
	except:
		pass

print "\nGrand totals:"
print "Cost: " + str(cost)
print "Paid: " + str(paid)
print "Balance: " + str(balance)

index = 0
if analyse=="closed":
	index = 0
elif analyse=="open":
	index = 1
elif analyse=="pending":
	index = 2
else:
	raise Exception("Incorrect argument for analysis!")
	

print "\n" + str(len(clientList[index])) + " client(s) are " + analyse + ":"
for client in clientList[index]:
	print client

if len(clientList[index]) > 0:		
	print "\nTotals for " + analyse + " entries:"
	print "Cost: " + str(analysis[index][0])
	print "Paid: " + str(analysis[index][1])
	print "Balance: " + str(analysis[index][2])

f.close()