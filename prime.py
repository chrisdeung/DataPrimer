num=2

while num<=100:
	
	isPrime = True
	i = 2
	while i < num:
		if num%i == 0:
			isPrime = False
			break
		i += 1
	
	if isPrime:
		print num
	num += 1