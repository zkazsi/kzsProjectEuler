def selfpowers(n,lastn):
        '''
        The series, 1p1 + 2p2 + 3p3 + ... + 10p10 = 10405071317.
        Find the last ten digits of the series, 1p1 + 2p2 + 3p3 + ... + 1000p1000.
        '''
        sumspow = 0
        for x in range(1,n+1):
                sumspow = sumspow + x**x
        print("Number of digits: ",len(str(sumspow)))
        print("Last digits: ",str(sumspow)[-lastn:])
