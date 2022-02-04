#String dans string
#Epreuve de l'eau, Exercice 6 : eau05.py

import sys

#fonctions
#recupere les premières lettres correspondant au nombre de lettre dans la regex


def split_txt(txt, nb):
    txt = str(txt)
    l = len(nb)
    i = 0
    new_txt = ""
    while i < l and len(txt) >= l:
        new_txt = new_txt+str(txt[i])
        i = i+1
    return new_txt

#supprime le premier caractere


def del_element(txt, regex):
    texte = ""
    i = 0
    l = len(txt)
    if l < len(regex):
        return 'not found'
    else:
        while i < l:
            if i == 0:
                i = i+1
            else:
                texte = texte+txt[i]
                i = i+1
    return texte

#regex dans la chaine de caractere


def is_in_str(txt, regex):
    txt = str(txt)
    part_txt = split_txt(txt, regex)
    result = ""
    if str(regex) == str(part_txt):
        result = True
    else:
        while del_element(txt, regex) != 'not found':
            txt = del_element(txt, regex)
            part_txt = split_txt(txt, regex)
            if regex == part_txt:
                result = True
                break
            else:
                result = False
    return result

#recuperation arguments


def args(sys_args):
    if len(sys_args) == 3:
        return True
    else:
        return False


#execution
nb_arg = args(sys.argv)
if nb_arg == True:
    txt = sys.argv[1]
    regex = sys.argv[2]
    result = is_in_str(txt, regex)
    print(result)
else:
    print('Error : you need two arguments')
    print('Error : you need two arguments')
