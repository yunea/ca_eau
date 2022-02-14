#Trie à bulle
#Epreuve de l'eau, Exercice 13 : eau12.py

import sys


def my_bubble_sort(array):
    print(array)
    i = len(array)-1
    print(i)
    j = 0
    new_array = []
    while i > 1:
        print('i= '+str(i))
        while j < (i-1):

            print('j= '+str(j))
            if array[j+1] < array[j]:
                a = array[j+1]
                array[j+1] = array[j]
                array[j] = a
                new_array.append(a)
            else:
                new_array.append(array[j])
            j = j+1
        i = i-1
    return (new_array)


if len(sys.argv) > 3:
    args = sys.argv
    args.pop(0)
    tab = my_bubble_sort(args)
    print(tab)
else:
    print("Error")
