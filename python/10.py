def isprime(startnumber):
    startnumber*=1.0
    if startnumber%2==0 and startnumber!=2:
        return False
    for divisor in range(3,int(startnumber**0.5)+1,2):
        if startnumber%divisor==0:
            return False
    return True

def sumprimes(n):
	x = 2
	sum = 0
	for x in range(2,n):
		if isprime(x):
			sum = sum + x
	return sum