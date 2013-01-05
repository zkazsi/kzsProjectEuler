def digitsum(nth):
	'''	215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
	What is the sum of the digits of the number 21000?'''
	
	n = str(2 ** nth)
	sum = 0
	v = -1
	while v < len(n)-1:
		v = v + 1
		sum += int(n[v])
	return sum
