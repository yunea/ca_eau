#Parametres a l'envers
#Epreuve de l'eau, Exercice 3 : eau02.py

import sys

#liste d'argument a l'envers et sans le titre de l'exo


def lenvers(list_arg):
    #initialisation des variables
    new_list = dict()
    i = 0
    c = 0
    l = len(list_arg)-1
    #passage de la list a l'envers
    while i < len(list_arg):
        new_list[i] = list_arg[l]
        i = i+1
        l = l-1

    #suppression du nom de l'exo du dictionnaire
    for a in new_list:
        if new_list[a] == 'eau02.py':
            c = a
    del new_list[c]
    #retourne la liste à l'envers
    return new_list


#affichage des arguments du dictionnaire
args = lenvers(sys.argv)
for a in args:
    print(args[a])
