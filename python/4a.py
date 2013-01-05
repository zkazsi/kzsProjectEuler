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
    print(len(lista))
    i = len(lista) - 1
    for sorszam in reversed(range(0,i)):
        div = 999
        if lista[sorszam] % div == 0:
            if len(str(lista[sorszam] // div)) == 3:
                print "Az eredmeny" + lista[sorszam]
                return lista[sorszam]
            elif div > 99:
                div = div - 1
                print lista[sorszam]
        elif div > 99:
            div = div - 1
    print("Nothing found")
    
