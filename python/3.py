def isprime(n):
    '''check if integer n is a prime
    prime numbers are only divisible by unity and themselves
    (1 is not considered a prime number by convention)
    '''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def maxprime(szam):
    ''' int -> int
	Find the largest prime factor of a composite number.
	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?
    '''
    primedivlist = []  
    newszam = szam
    n = 2
    while not n > newszam:
        if isprime(n) == True and newszam % n == 0:
            primedivlist.append(n)
            newszam = newszam / n
            n = n + 1
        else:
            n = n + 1
    print(primedivlist)
    return max(primedivlist)
        
