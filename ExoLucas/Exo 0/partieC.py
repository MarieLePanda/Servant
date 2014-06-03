#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lug13995
#
# Created:     15/04/2014
# Copyright:   (c) lug13995 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    palindrome()

    pass

def palindrome():

    mot = input("Saisir un mot")
    mot = str.lower(mot)
    longueur = len(mot)
    palindrome=True
    j=longueur-1
    i=0
    for i in range (i,longueur//2 or palindrome==False):

        premier=mot[i]
        dernier=mot[j]
        j=j-1
        if (premier!=dernier):

            palindrome=False

    if (palindrome==True):
        print(mot, " est un palindrome")

    else:
        print(mot, "n'est pas un palindrome")

    pass

def partieC():
    tabA = {"nombre" : 1, "mot" : "mot", "pi" : 3.14}

    user = input("Saissisez un mot")

    if(tabA.get(user)) :
        print("La valeur associée à  ", user, " est ", tabA[user])
    else :
        print(user + " n'est pas une clé valide")

    pass
if __name__ == '__main__':
    main()
