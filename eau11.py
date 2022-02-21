#difference minimum absolue
#Epreuve de l'eau, Exercice 12 : eau11.py

import sys

#tableau des differences


def tab_min(tab):
    res = []
    for n in tab:
        for m in tab:
            if n == m:
                continue
            else:
                res.append(int(n)-int(m))
    return res

#chercher le min des differences


def find_min(tab):
    b = []
    for n in tab:
        if n < 0:
            b.append(n*(-1))
    for n in b:
        for m in tab:
            if n == (-m):
                tab.append(n)
        tab.remove(-n)
    a = tab[0]
    for n in tab:
        if a > n:
            a = n
    return a

#arg doit etre int


def is_int(tab):
    try:
        for arg in tab:
            int(arg)
        return True
    except:
        return False


#main
#minimum 2 arguments entre par l'utilisateur
if len(sys.argv) > 2:
    tab = sys.argv
    tab.pop(0)
    isInt = is_int(tab)
    if isInt == True:
        tabMin = tab_min(tab)
        findMin = find_min(tabMin)
        print(findMin)
    else:
        print("Error")
else:
    print("Error")
