def maxpaliw(egy,ketto):
        palik = []
        while egy < 1000:
                while ketto < 1000:
                        palik.append(egy * ketto)
                        ketto = ketto + 1
                egy = egy + 1
        print(max(palik))
        print(palik)

def maxpalif(a,b):
        '''Project Euler, Problem no 4
        A palindromic number reads the same both ways. The largest palindrome 
        made from the product of two 2-digit numbers is 9009 = 91 x 99
        Find the largest palindrome made from the product of two 3-digit numbers.
        This code computes largest in the range (a,b), but first prints out complete palindrome list.
        '''
        palindromes = []
        for x in range(min(a,b), max(a,b)):
                for z in range(min(a,b), max(a,b)):
                        if str(x * z) == str(x * z)[::-1]:
                                palindromes.append(x * z)
        print(palindromes)
        return max(palindromes)
