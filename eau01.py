#Combinaisons de 2 nombres
#Epreuve de l'eau, Exercice 2 : eau01.py

#test si les chiffres sont les memes
def number_same(a, b):
    if int(a) == int(b):
        return True
    return False


#test si la combinaison de 2 nombres est deja dans la liste
def in_list(l, a, b):
    number = get_number(b, a)
    #print("NUMBER : " + number)
    for n in l:
        #print(n)
        if str(number) == str(n):
            return True
    return False


#passe a la combinaison suivante
def next_number(a, b):
    if b < 99:
        b = b + 1
    else:
        a = a + 1
        b = 1
    return a, b


#renvoie le nombre sous la bonne forme
def get_number(a, b):
    a = str(a)
    b = str(b)
    if len(a) < 2:
        a = "0"+str(a)
    if len(b) < 2:
        b = "0"+str(b)
    number = str(a)+" "+str(b)
    return number


#initialisation des variables
nb1 = 00
nb2 = 00
list_number = list()

while nb1 < 99:
    if number_same(nb1, nb2) == True:
        nb1, nb2 = next_number(nb1, nb2)

    elif in_list(list_number, nb1, nb2) == True:
        nb1, nb2 = next_number(nb1, nb2)

    else:
        number = get_number(nb1, nb2)
        list_number.append(number)
        nb1, nb2 = next_number(nb1, nb2)

#affichage de la liste sous forme de string
list_number_str = [str(a) for a in list_number]
print(', '.join(list_number_str))
