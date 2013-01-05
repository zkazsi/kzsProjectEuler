from math import sqrt

def isprime(startnumber):
    startnumber*=1.0
    if startnumber%2==0 and startnumber!=2:
        return False
    for divisor in range(3,int(startnumber**0.5)+1,2):
        if startnumber%divisor==0:
            return False
    return True	
		
def dividebyall(div):
	'''
	What is the smallest number divisible by each of the numbers 1 to 20?
	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any 
	remainder.
	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
	Logic:
		1) find prime factors of divisor (eg. 20)
		2) find lowest common multiple of these (prime) factors = multiple
		3) check if this number can be divided (w/o remainder) by all numbers below divisor
		4) new number = number + multiple
		5) loop from 3
	'''
	primelist = []
	for a in range(div+1):
		if isprime(a) == True:
			primelist.append(a)
	print("List of the primes: ",primelist)
	lmc = 1
	for item in primelist:
		lmc = lmc * item
	print("Lowest multiple is ",lmc)
	
	i = lmc
	while 1:
		i = i + lmc
		ok = 1
		for x in range(1,div+1):
			if i % x != 0:
				ok = 0
				break
		if ok == 1:
			number = i
			break

	print("What is the smallest positive number that is evenly divisible\n by all of the numbers from 1 to ",div,"?")
	print("Result is:",number)
