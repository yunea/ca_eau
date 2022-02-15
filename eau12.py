#Trie à bulle
#Epreuve de l'eau, Exercice 13 : eau12.py

import sys


def my_bubble_sort(array):
    i = (len(array)-1)
    j = 0
    x = 0
    c = True
    while i > 1:
        c = True
        print("i="+str(i))
        print("j="+str(j))
        while j < i:

            print(array)
            if (array[j] > array[j+1]):

                x = array[j]
                array[j] = array[j+1]
                array[j+1] = x
                c = False
            j = j+1
        i = i-1

        print("c="+str(c))
        if c == True:
            return (array)


if len(sys.argv) > 3:
    args = sys.argv
    args.pop(0)
    print(args)
    tab = my_bubble_sort(args)
    print(tab)
else:
    print("Error")
