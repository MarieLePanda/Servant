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
    #print(prime_numbers(10))
    #print(factorial(20))
    display_file("C:\\Users\\lug13995\\Desktop\\ESGI\\la_vie.java")
    #stat_file("C:\\Users\\lug13995\\Desktop\\ESGI\\Portable Python 3.2.5.1\\Exo 1\\panda.txt")
    pass

def prime_numbers(nb):
    """Renvoie les nombres premier inferieur au nombre entre en parametre"""
    tab = []
    while(nb > 0) :
        nb = nb - 1
        tab.append(nb)
    return tab

    pass

def factorial(n):
    if n < 2 :
       return 1
    return factorial(n-1)*n

    pass

def display_file(nameFile) :
    """Affiche le contenue du fichier passe en parametre"""
    nbLine = 1
    myFile = open(nameFile, "r")
    for line in myFile:
        print(nbLine, " ",line.replace("\n", ""))
        nbLine = nbLine + 1
    myFile.close

    pass

def stat_file(nameFile):

    tabB = {}
    myFile = open(nameFile, "r")
    for line in myFile:
        for l in line.split() :
            if(l in tabB.keys()) :
                tabB[l] =  tabB[l] + 1
            else :
                tabB[l] = 1

        for k,v in tabB.items() :
            print(k, " -> ", v)

    pass

if __name__ == '__main__':
    main()
