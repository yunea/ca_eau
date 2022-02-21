#Index wanted
#Epreuve de l'eau, Exercice 11 : eau10.py

import sys

#cherche regex dans tableau


def in_tab(tab, car):
    res = False
    for i in tab:
        if str(i) == str(car):
            res = True
    return res

#cherche l'index de la premiere apparition de la regex


def find_index(tab, car):
    i = 0
    if in_tab(tab, car) == True:
        for c in tab:
            if str(c) == str(car):
                break
            i = i+1
    return i

#recuperer dernier arg == regex


def recup_arg(tab):
    l = len(tab)
    arg = tab[l-1]
    return arg

#recuperer tab sans le dernier arg


def recup_tab(tab):
    tab.pop(0)
    l = len(tab)
    tab.pop(l-1)
    return tab


if len(sys.argv) >= 3:
    reg = recup_arg(sys.argv)
    chaine = recup_tab(sys.argv)
    if in_tab(chaine, reg) == True:
        index = find_index(chaine, reg)
        print(index)
    else:
        print(-1)
else:
    print("Error : 2 arguments needed")
