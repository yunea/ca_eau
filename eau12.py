#Trie à bulle
#Epreuve de l'eau, Exercice 13 : eau12.py

import sys


def my_bubble_sort(array):
    i = (len(array)-1)
    j = 0
    x = 0
    while i >= 1:
        while j <= i-1:
            if (array[j] > array[j+1]):
                x = array[j]
                array[j] = array[j+1]
                array[j+1] = x
            j = j+1
        i = i-1
        j = 0
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
        res = my_bubble_sort(args)
        res_str = [str(a) for a in res]
        print(' '.join(res_str))
    else:
        print("Error")
else:
    print("Error")
