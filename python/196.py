def primetriplets(a,b):
        '''
		Problem 196: Prime Triplets
		Build a triangle from all positive integers in the following way:

		 1
		 2  3
		 4  5  6
		 7  8  9 10
		11 12 13 14 15
		16 17 18 19 20 21
		22 23 24 25 26 27 28
		29 30 31 32 33 34 35 36
		37 38 39 40 41 42 43 44 45
		46 47 48 49 50 51 52 53 54 55
		56 57 58 59 60 61 62 63 64 65 66
		. . .

		Each positive integer has up to eight neighbours in the triangle.

		A set of three primes is called a prime triplet if one of the three primes has the other two as neighbours in the triangle.

		For example, in the second row, the prime numbers 2 and 3 are elements of some prime triplet.

		If row 8 is considered, it contains two primes which are elements of some prime triplet, i.e. 29 and 31.
		If row 9 is considered, it contains only one prime which is an element of some prime triplet: 37.

		Define S(n) as the sum of the primes in row n which are elements of any prime triplet.
		Then S(8)=60 and S(9)=37.

		You are given that S(10000)=950007619.

		Find  S(5678027) + S(7208785).
		
		STEPS:
		1) Find first element of row:
			a) increase by row = rownum -1
		2) Check numbers one by one:
				while element < (first + rownum-1)
		# 2) Create List: all elements of that row
			# - [first:first+rownum]
		3) Check for each, if prime number
			element = element +1
			isprime(element)
		4) If prime:
			a) Tell position
			b) check each neighbor, if prime 
				[-1], [+1], [row-1][element-1]:[row-1][element+1], [row+1][element-1]:[row+1][element+1]:
					ATT: elements 2nd to last and last of each row only 7 / 5 neighbors to be checked!!!
			c) if neighbor prime:
				- increase counter: +1
				- count neighbor primes (up to 2): member of prime triplet (at least)
			d) if member of prime triplet:
				- ADD TO SUM
			e) if no prime triplet: NEXT
		'''
		
	
def isprime(startnumber):
    startnumber*=1.0
    if startnumber%2==0 and startnumber!=2:
        return False
    for divisor in range(3,int(startnumber**0.5)+1,2):
        if startnumber%divisor==0:
            return False
    return True
	
def findelement(rownum, elemno):
        first = 1
        for szamlalo1 in range(1,rownum):
                first = first + szamlalo1
        # print("First element of row is ",first)
        if elemno < rownum+1:
                element = first + elemno
                # print("The element we're searching for is ",element)
                return element
        else:
             print("The element we're searching for doesn't exist in this row")   

        

def checkprimes(rownum):
	primesinrow = []
	if findelement(rownum,0) % 2 == 0:
		eno = 1
	else:
		eno = 0
	if findelement(rownum,rownum) % 2 == 0:
		lno = rownum - 1
	else:
		lno = rownum
	for element in range(findelement(rownum,eno),findelement(rownum,lno)):
		if isprime(element):
			primesinrow.append(element)
	print("The primes in this row are: ")
	return primesinrow


def checkifprime(rownum,elemno):
	return isprime(findelement(rownum,elemno))
	
# def checkrow(rownum):
#	for elem in range(findelement(rownum,0),findelement(rownum,rownum)):
#		if isprime(elem):
#			checkneighbors(elem)
#			if isprimetriplet(elem):
#				sum = sum + elem
#	return sum
