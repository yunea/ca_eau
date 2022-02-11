#difference minimum absolue
#Epreuve de l'eau, Exercice 12 : eau11.py

import sys


def tab_min(tab):
    i = 1
    res = []
    for n in tab:
        if i > len(tab)-1:
            break
        else:
            b = int(n)-int(tab[i])
            res.append(b)
            i = i+1
    return res


def find_min(tab):
    print(tab)
    for n in tab:
        print(n)
        if n < 0:
            print("nnn : "+str(n))
            tab.remove(n)
            n = n*(-1)
            tab.append(n)
    a = tab[0]
    for n in tab:
        print("n :"+str(n))
        if a > n:
            print("a : "+str(a))
            a = n
    #print(tab)
    return a


def is_int(tab):
    try:
        for arg in tab:
            int(arg)
        return True
    except:
        return False


tab = sys.argv
tab.pop(0)
isInt = is_int(tab)
if isInt == True:
    tabMin = tab_min(tab)
    findMin = find_min(tabMin)
    print(findMin)
else:
    print("Error")
