#Trie par ordre ascii
#Epreuve de l'eau, Exercice 15 : eau14.py

import sys


def to_ascii(tab_str):
    mot = ""
    tab_ascii = list()
    i = 0
    for chaine in tab_str:
        for car in chaine:
            mot = str(mot)+str(ord(car))+"."
            print(str(mot))
        tab_ascii.append(str(mot))
        i = i+1
    return tab_ascii


def tri_ascii(tab_ascii):
    i = 1
    for chaine in tab_ascii:
        car = chaine.split(".")
        car2 = tab_ascii[i].split(".")


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
print(new_args)
