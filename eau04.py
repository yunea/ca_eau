#Prochain nombre premier
#Epreuve de l'eau, Exercice 5 : eau04.py

import sys

#fonctions
#bon nombre d'arguments donnes par l'utilisateur


def nb_arg(args):
    if (len(args) == 2):
        return True
    else:
        return False

#l'argument est un entier positif


def is_int(arg):
    try:
        a = int(arg)
        if a < 0:
            return False
        else:
            return True
    except:
        return False

#le nombre en parametre est un nombre premier


def is_nb_premier(nombre):
    nombre = int(nombre)
    if (nombre == 0 or nombre == 1):
        return False
    else:
        i = 2
        while (int(i) < int(nombre) and (int(nombre) % int(i)) != 0):
            i = i+1
        if(int(i) == int(nombre)):
            return True
        else:
            return False

#trouve le nombre premier suivant


def next_nb_premier(nombre):
    nombre = int(nombre)+1
    nb_premier = is_nb_premier(nombre)
    if nb_premier == False:
        nombre = int(nombre)+1
        while is_nb_premier(nombre) == False:
            nombre = nombre + 1
        return nombre
    else:
        return nombre


#initialisation des variables
args = sys.argv
arg = ""
nombre = 0

#tests et gestion des erreurs
if nb_arg(args) == True:
    arg = sys.argv[1]
    if is_int(arg) == True:
        nombre = next_nb_premier(arg)
        print(str(nombre))

    else:
        print("-1")
else:
    print("-1")
