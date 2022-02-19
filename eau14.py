#Trie par ordre ascii
#Epreuve de l'eau, Exercice 15 : eau14.py

import sys


def to_ascii(tab_str):
    mot = ""
    tab_ascii = {}
    i = 0
    for chaine in tab_str:
        for car in chaine:
            mot = str(mot)+str(ord(car))+"."
        tab_ascii[str(chaine)] = str(mot)
        mot = ""
        i = i+1
    return tab_ascii


def tri_ascii(array):
    tab_ascii = {}
    res = []
    j = 0
    for key in array:
        tab_ascii[j] = array[key]
        j = j+1
    i = (len(tab_ascii)-1)
    x = 0
    k = 0
    j = 0
    #mise en ordre ascii
    while i >= 1:
        while j <= i-1:
            chaine1 = tab_ascii[j]
            chaine2 = tab_ascii[j+1]
            car1 = chaine1.split(".")
            car2 = chaine2.split(".")
            car1.remove('')
            car2.remove('')
            k = 0
            while (k < len(car1) and k < len(car2)):
                if int(car1[k]) > int(car2[k]):
                    x = tab_ascii[j]
                    tab_ascii[j] = tab_ascii[j+1]
                    tab_ascii[j+1] = x
                k = k+1
            j = j+1
        i = i-1
        j = 0
    print("tab ascii :")
    print(tab_ascii)
    #mise en ordre avec les arguments
    j = 0
    for car_ascii in tab_ascii:
        for key in array:
            if str(tab_ascii[car_ascii]) == str(array[key]):
                res.append(key)
                j = j+1
    return (res)


def comparer(a, b):
    if int(a) > int(b):
        return a
    elif int(a) < int(b):
        return b
    else:
        return "egaux"


args = sys.argv
args.pop(0)
new_args = to_ascii(args)
res = tri_ascii(new_args)
res_str = [str(a) for a in res]
print(' '.join(res_str))
