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

def main():
    print("Partie B")
    tabA = {"nombre" : 1, "mot" : "mot", "pi" : 3.14}

    print("Ajouter")
    print("Pas compris la question")

    print("Remplacer")
    tabA["nombre"] = 42
    print(tabA)

    print("Supprimmer")
    del tabA["pi"]
    print(tabA)

    pass

if __name__ == '__main__':
    main()
