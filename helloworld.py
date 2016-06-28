import sys

if len(sys.argv) > 2:
	print "Hello " + sys.argv[1]
	timeTable = int(sys.argv[2])
	for i in xrange(1, 11):
		print str(timeTable) + " x " + str(i) + " = " + str(timeTable*i)
else:
	print "Not enough arguments!"