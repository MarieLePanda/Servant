#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lug13995
#
# Created:     18/04/2014
# Copyright:   (c) lug13995 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    print("B1 Liste des carrés jusqu'a 100")
    listCompr = [n * n for n in range(0, 100)]
    for e in listCompr:
        print(e)

    print("B2 Liste des carrés inférieur a 100")

    listCompr = [n * n for n in range(0, 100) if n * n  < 100 ]
    for e in listCompr:
        print(e)

    print("B3 Liste des nombres qui inférieur à 100 qui sont divisible par 7")
    listCompr = [n for n in range(0, 200) if n % 7 == 0 and n  < 100]
    for e in listCompr:
        print(e)

    print("B4")
    pass

if __name__ == '__main__':
    main()
