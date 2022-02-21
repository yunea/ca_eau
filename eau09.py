#Entre min et max
#Epreuve de l'eau, Exercice 10 : eau09.py

import sys


def min_to_max(min, max):
    tab_num = []
    min = int(min)
    max = int(max)
    while min < max-1:
        tab_num.append(min+1)
        min = min+1
    return tab_num


def is_max(a, b):
    if a > b:
        return a
    else:
        return b


def is_min(a, b):
    if a > b:
        return b
    else:
        return a


def is_int(a, b):
    try:
        int(a)
        int(b)
        return True
    except:
        return False


tab = []

if len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    int_res = is_int(arg1, arg2)
    if int_res == True:
        min = is_min(arg1, arg2)
        max = is_max(arg1, arg2)
        tab.append(int(min))
        tab1 = min_to_max(min, max)
        for n in tab1:
            tab.append(n)
        str_tab = " ".join(map(str, tab))
        print(str_tab)
    else:
        print("Error integer needed")
else:
    print("Error two arguments needed")
