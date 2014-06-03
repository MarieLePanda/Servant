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

    liste = [1,2,3,4,5,6,7,8,9]
    for l in liste :
        print(l)

    tabA = {"nombre" : 1, "mot" : "mot", "pi" : 3.14}

    for t in tabA :
        print("cle : ", t, "valeur : ", tabA[t])
    tabB = {}
    val = input("Saissisez une phrase")

    for l in val :
        tabB[l] = val.count(l)

    for k,v in tabB.items() :
        print(k, " -> ", v)


    pass

if __name__ == '__main__':
    main()
