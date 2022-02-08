#Majuscule sur deux
#Epreuve de l'eau, Exercice 7 : eau06.py

import sys


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

#passage en majuscule


def maj(txt):
    i = 0
    result = ""
    for letter in txt:
        if letter == " ":
            result = result+str(letter)
            continue
        elif i % 2 == 0:
            letter = to_maj(letter)
            result = result+str(letter)
            i = i+1
        else:
            result = result+str(letter)
            i = i+1
    return result

#test arg is string


def is_string(arg):
    try:
        int(arg)
        return False

    except:
        return True


#initialisation variable
arg = sys.argv[1]
#test et execution du code
if len(sys.argv) == 2:
    if is_string(arg) == True:
        result = maj(arg)
        print(result)
    else:
        print("Error : argument must be string")
else:
    print('Error : one argument needed')
