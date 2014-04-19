#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lug13995
#
# Created:     25/03/2014
# Copyright:   (c) lug13995 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def partieA():
    liste = [1,2,3,4,5,6,7,8,9]
    print("=================A1================")
    print(liste)
    print("=================A2================")
    print("Premier élément")
    print(liste[0])
    print("Troisème élément")
    print(liste[2])
    print("Dernier élément")
    print(liste[-1])
    print("=================A3================")
    print("Trois premier éléments et trois dernier éléments")
    listePrem = [liste[0], liste[1], liste[2]]
    listeDern = [liste[-1], liste[-2], liste[-3]]
    print(listePrem, listeDern)
    print("élément d'indice pair")
    print(liste[::2])
    print("=================A4================")
    liste.append(10)
    liste.insert(0, 0)
    print(liste)
    print("=================A5================")
    print("Remplacer les éléments 1, 2 et 3")
    liste[1] = "un"
    liste[2] = "deux"
    liste[3] = "trois"
    print(liste[1], liste[2], liste[3])
    print("=================A6================")
    print("Supprimer le premier élément")
    del liste[0]
    print(liste)
    print("supprimer le dernier élément")
    del liste[-1]
    print(liste)
    print("supprimer tous les éléments multiple de 3")
    del liste[::3]
    print(liste)
    print("=================A7================")
    print("Liste inversée")
    liste2 = liste
    liste2.reverse()
    print(liste2)
    print("3 fois le début de liste")
    liste3 = liste[0:3] + liste[0:3] + liste[0:3]
    print(liste3)


def main():
    pass
    print("partie A")
    partieA()


if __name__ == '__main__':
    main()
