def ispalindrome(w):
    return str(w) == str(w)[::-1]

def listpalindrome(last):
	lista = []
	first = 10001
	for sz in range(first,last):
		if ispalindrome(sz) == True:
			lista.append(sz)
			sz = sz - 1
		else:
			sz = sz - 1
	print lista
	return lista

def findlastpali(last):
    listpalindrome(998001)
    i = len(lista) - 1
    for sorszam in reversed(range(0,i)):
        div = 999
        if lista[i] % div == 0:
                if len(str(lista[i] // div)) == 3:
                    return lista[i]
                elif div > 99:
                    div = div - 1
        elif div > 99:
            div = div - 1
