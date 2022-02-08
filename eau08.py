#Chiffres only
#Epreuve de l'eau, Exercice 9 : eau08.py

import sys


def is_int(arg):
    tab_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    tab_res = []
    res = False
    resultat = True
    for n in arg:
        for i in tab_num:
            print("i:"+str(i)+" n:"+str(n))
            if n == i:
                res = True
                i = 0
            else:
                res = False
        tab_res.append(res)
    print(tab_res)
    for r in tab_res:
        if r == False:
            resultat = False
            break
        else:
            resultat = True
    return resultat


arg = sys.argv[1]


print(is_int(arg))
