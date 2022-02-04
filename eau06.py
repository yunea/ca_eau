#Majuscule sur deux
#Epreuve de l'eau, Exercice 6 : eau05.py

import sys

#passage en majuscule


def maj(txt):
    i = 0
    result = ""
    for letter in txt:
        if letter == " ":
            result = result+str(letter)
            continue
        elif i % 2 == 0:
            letter = letter.upper()
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
