def kettes(x):
	''' Project Euler, Problem no 2
	By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
	find the sum of the even-valued terms.
	
	'''
	x0 = 0
	x1 = 1
	x = 0
	osszeg = 0
	while x < 4000000:
		x = x0 + x1
		x0 = x1
		x1 = x
		if x % 2 == 0:
			osszeg = osszeg + x

	return osszeg
