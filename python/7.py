def isprime(startnumber):
    startnumber*=1.0
    if startnumber%2==0 and startnumber!=2:
        return False
    for divisor in range(3,int(startnumber**0.5)+1,2):
        if startnumber%divisor==0:
            return False
    return True

def xthprime(xth,rangeend):
    '''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    '''
    primes = [2, 3]
    for p in range(3,rangeend,2):
        while len(primes) < xth:
            p = p + 2
            if isprime(p):
                primes.append(p)
    print(primes)
    
	
