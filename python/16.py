def digitsum(nth):
	'''	215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
	What is the sum of the digits of the number 2p1000?'''
	
	n = str(2 ** nth)
	sum = 0
	for v in range(len(n)):
		sum += int(n[v])
	return sum