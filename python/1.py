def egyes(n):
	''' Project Euler, Problem no 1
	Add all the natural numbers below one thousand that are multiples of 3 or 5.
	
	Elegant, short (1-liner solution in Python:
	print sum([x for x in range(1,1000) if x % 5 == 0 or x % 3 == 0])
	'''
        osszeg = 0
        while n < 1000:
                if n % 3 == 0:
                        osszeg = osszeg + n
                        n = n + 1
                elif n % 5 == 0:
                        osszeg = osszeg + n
                        n = n + 1
                else:
                        n = n + 1
        return osszeg
