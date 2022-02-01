#Combinaisons de 3 chiffres
#Epreuve de l'eau, Exercice 1 : eau00.py

#les trois chiffres sont les memes
def is_same(number):
    n = str(number)
    a = n[0]
    b = n[1]
    c = n[2]
    if (a != b and b != c and c != a):
        return False
    else:
        return True

#le nombre est deja dans la liste


def is_in_list(n_list, x):
    if len(n_list) < 1:
        return False
    else:
        for nb in n_list:
            if nb == x:
                return True
        return False

#les chiffres du nombre forment deja un autre nombre


def nb_in_list(list_number, x):
    l = list()
    count = 0
    for a in str(x):
        l.append(a)
    for nb in list_number:
        nb = str(nb)
        count = 0
        if str(nb[0]) == str(l[0]) or str(nb[0]) == str(l[1]) or str(nb[0]) == str(l[2]):
            count = count+1
        if str(nb[1]) == str(l[0]) or str(nb[1]) == str(l[1]) or str(nb[1]) == str(l[2]):
            count = count+1
        if str(nb[2]) == str(l[0]) or str(nb[2]) == str(l[1]) or str(nb[2]) == str(l[2]):
            count = count+1
        if count == 3:
            return True
    return False

#passage au nombre suivant


def next_number(number):
    n = int(number)+1
    if len(str(n)) == 1:
        n = "00"+str(n)
    if len(str(n)) == 2:
        n = "0"+str(n)
    return n


#initialisation des variables
number = "000"

list_number = list()
same = False
inlist = False
nblist = False
x = 0

#boucle qui va jusqu'au plus grand nombre a trois chiffres
while x < 999:
    x = x+1

    #récupération des valeurs des tests
    same = is_same(number)
    inlist = is_in_list(list_number, number)
    nblist = nb_in_list(list_number, number)

    #tests par rapport au resultat
    if (same == True):
        number = next_number(number)
    elif (inlist == True):
        number = next_number(number)
    elif (nblist == True):
        number = next_number(number)
    else:
        list_number.append(number)
        number = next_number(number)

#affichage de la liste sous forme de string
list_number_str = [str(a) for a in list_number]
print(', '.join(list_number_str))
