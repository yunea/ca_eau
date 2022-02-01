#Parametres a l'envers
#Epreuve de l'eau, Exercice 4 : eau03.py

import sys

#erreur nombre d'arguments


def len_error(args):
    if len(args) != 2:
        return True
    else:
        return False

#erreur si arg string ou <0


def arg_error(args):
    try:
        a = int(args[1])
        if a < 0:
            return True
        return False
    except:
        return True

#recuperation de l'argument


def recup_arg(args):
    a = args[1]
    return a

#trouver l'element de la suite fibonacci demande


def find_fibo(fibo_list, arg):
    i = 0
    j = (int(arg)-len(fibo_list)+1)
    n = 0
    if int(arg) < len(fibo_list):
        return fibo_list[arg]
    else:
        while i < j:
            l = len(fibo_list)-1
            k = int(fibo_list[str(l)])
            m = int(fibo_list[str(l-1)])
            n = k+m
            fibo_list[str(l+1)] = int(n)
            i = i+1
        return n


#initialisation des variables
debut_fibo = {"0": 0, "1": 1}
number = -1

while True:
    if len_error(sys.argv) == True:
        print("-1")
        break
    elif arg_error(sys.argv):
        print("-1")
        break
    else:
        arg = recup_arg(sys.argv)
        number = find_fibo(debut_fibo, arg)
        break

#affichage de l'element
if number != -1:
    print(number)
