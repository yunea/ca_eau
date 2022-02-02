#String dans string
#Epreuve de l'eau, Exercice 6 : eau05.py

import sys


def split_txt(txt, nb):
    txt = str(txt)
    nb = int(nb)
    i = 0
    new_txt = ""
    while i < nb:
        new_txt = new_txt+str(txt[i])
    return new_txt


def del_element(txt):
    texte = ""
    i = 0
    while i < len(txt):
        if i == 0:
            continue
        else:
            texte = texte+txt[i]
    print('Texte : '+str(texte))
    return texte


def is_in_str(txt, regex):
    txt = str(txt)
    reg = str(regex)
    part_txt = split_txt(txt, regex)
    result = ""
    if reg == part_txt:
        result = True
    else:
        del txt[0]
        result = False

    return result


def args(sys_args):
    if len(sys_args) == 3:
        return True
    else:
        return False


nb_arg = args(sys.argv)
if nb_arg == True:
    txt = sys.argv[1]
    regex = sys.argv[2]
    result = is_in_str(txt, regex)
    print(result)
else:
    print('Error : you need two arguments')
