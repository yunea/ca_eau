#Trie par selection
#Epreuve de l'eau, Exercice 14 : eau13.py

import sys


def my_select_sort(array):
    n = len(array)
    i = 0
    while i <= (n-2):
        min = i
        j = i+1
        while j <= (n-1):
            if (array[j] < array[min]):
                min = j
            j = j+1
        if i != min:
            x = array[min]
            array[min] = array[i]
            array[i] = x
        i = i+1
    return (array)


def is_int(args):
    try:
        for arg in args:
            int(arg)
        return True
    except:
        return False


if len(sys.argv) > 2:
    args = sys.argv
    args.pop(0)
    if is_int(args) == True:
        res = my_select_sort(args)
        res_str = [str(a) for a in res]
        print(' '.join(res_str))
    else:
        print("Error")
else:
    print("Error")
