#Majuscule
#Epreuve de l'eau, Exercice 8 : eau07.py

import sys


def is_string(arg):
    try:
        int(arg)
        return False

    except:
        return True


def nb_arg(args):
    b = False
    if len(args) == 2:
        b = True
    return b


#change min to maj
def to_maj(letter):
    l_min = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    l_maj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    count_index = 0
    is_maj = False
    for l in l_min:
        if l == letter:
            break
        else:
            count_index = count_index+1
    for l in l_maj:
        if l == letter:
            is_maj = True
    if count_index >= 26:
        is_maj = True
    if is_maj == True:
        new_letter = letter
    else:
        new_letter = l_maj[count_index]
    return new_letter

#passage des majuscules 1 sur 2


def majuscule(chaine):

    new_chaine = ""
    result = ""
    i = 0
    tab = []
    tab.append(0)
    for l in chaine:
        if l == " ":
            tab.append(i+1)
            new_chaine = new_chaine+l
        elif l == "\n":
            tab.append(i+1)
            new_chaine = new_chaine+l
        elif l == "\t":
            tab.append(i+1)
            new_chaine = new_chaine+l
        elif l == "\r":
            tab.append(i+1)
            new_chaine = new_chaine+l
        else:
            new_chaine = new_chaine+l
        i = i+1
    i = 0
    for l in new_chaine:
        for j in tab:
            if i == j:
                l = to_maj(l)
        result = result+l
        i = i+1

    return result


#main
arg = sys.argv[1]
if nb_arg(sys.argv) == True:
    if is_string(arg) == True:
        chaine = majuscule(arg)
        print(chaine)
    else:
        print("Error : argument must be a string")
else:
    print("Error : one argument needed")
