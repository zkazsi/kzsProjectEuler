def sumsqdiff(a,b):
        '''
        Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

        Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
        '''
        sumsquares = 0
        numsum = 0
        for x in range(a,b+1):
                sumsquares = sumsquares + x**2
        print("The sum of squares is: ",sumsquares)
        for y in range(a,b+1):
                numsum = numsum + y
        sqsums = numsum ** 2
        print("The square of sums is: ",sqsums)
        print("The FINAL result (difference) is: ", sqsums - sumsquares)
        return sqsums - sumsquares
