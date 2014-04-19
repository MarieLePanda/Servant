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
import random


def main():

    cardSet = loadCardSet("C:\\Users\\MKSJ\\Documents\\GitHub\\Servant\\Exo 2\\cardSet")
    playerOne = initPlayer(cardSet)
    playerTwo = initPlayer(cardSet)

    print("Player one")
    for cardPlayer in playerOne["field"]:
        printCard(cardPlayer)
    print("Player two")
    for cardPlayer in playerTwo["field"]:
        printCard(cardPlayer)

    for i in range(10):
        if i % 2 == 0 :
            playTrun(playerOne, playerTwo)
        else :
            playTrun(playerTwo, playerOne)
    print("Player one")
    for cardPlayer in playerOne["field"]:
        printCard(cardPlayer)

    print("Player two")
    for cardPlayer in playerTwo["field"]:
        printCard(cardPlayer)


    pass

def loadCard(name, health, attack, cost) :
    """Create servant card"""

    cardServant = {"name" : name, "health" : health, "attack" : attack, "cost" : cost}
    return cardServant

    pass

def printCard(servant, displayMana = True) :
    """display servant card"""

    if(displayMana):
        print("name " , servant["name"] ,
        "(" , servant["attack"] , "/" , servant["health"] , ") : ",
        servant["cost"]
         )
    else:
        print("name " , servant["name"] ,
        "(" , servant["attack"] , "/" , servant["health"] , ")")

    pass

def fight(servantOne, servantTwo) :
    """Servant one hit servant two"""

    servantTwo["health"] -= servantOne["attack"]

    pass

def loadCardSet(nameFile):
    """Load a card set from a file"""

    file = open(nameFile)
    listServant = []
    for line in file:
        cardSet = []
        for word in line.split():
            if word.isnumeric():
                cardSet.append(int (word))
            else:
                cardSet.append(word)
        listServant.append(loadCard(cardSet[0], cardSet[2], cardSet[1], cardSet[3]))
    file.close
    return listServant

    pass

def initPlayer(serviteur):
    """Create player witch hand of 4 card"""

    hand = []
    while len(hand) < 4 :
        numCard = random.randint(0, len(serviteur) - 1)
        if(serviteur[numCard] not in hand) :
            hand.append(serviteur[numCard])
            serviteur.remove(serviteur[numCard])
    player = {"health" : 30, "mana" : 1, "hand" : hand, "field" : []}
    return player

    pass

def playTrun(player, ennemy):
    """Player can send servant to the field and attack ennemy servant"""

    choice = False

#Test si le joueur peut attaquer

    if len(player["field"]) == 0 :
        print("Vous n'avez aucun serviteur pour attaquer")
    elif len(ennemy["field"] ) == 0 :
        print("Il n'y a aucune serviteur ennemie a attaquer")
    else :
        print("Avec quel serviteur voulez vous attaquer ?")
        nameServantAttack = ""

#Phase d'attaque

        servantCanAttack = list(player["field"])
        while 0 < len(servantCanAttack) :
            print("Nombre de tour d'attaque : ", len(servantCanAttack))
            print("Avec quel serviteur voulez vous attaquer ?")
            nameServantAttack = ""
#Liste des serviteurs du joueur sur le champ de bataille

            print("Liste des servants sur le terrain")
            for cardPlayer in player["field"] :
                printCard(cardPlayer)
            print("Liste de vos serviteur sur le terrain qui peuvent attaquer")
            for cardPlayer in servantCanAttack :
                printCard(cardPlayer)
            while choice == False :
                nameServantAttack = input("Choisisez le nom du serviteur qui va attaquer")
                for card in servantCanAttack :
                    if nameServantAttack == card["name"] :
                        choice = True
            choice = False
            servantAttack = ""
            for servant in servantCanAttack :
                if servant["name"] == nameServantAttack:
                    servantAttack = servant
                    servantCanAttack.remove(servant)

#Liste des serviteurs de l'ennemie sur le champ de bataille

            print("Liste des serviteur adverse sur le terrain")
            for cardPlayer in ennemy["field"] :
                printCard(cardPlayer)
            print("Quel serviteur ennemy voulez vous attaquer ?")
            nameServantTarget = ""
            while choice == False:
                nameServantTarget = input("Choisisez le nom du serviteur a attaquer")
                for card in ennemy["field"] :
                    if nameServantTarget == card["name"] :
                        choice = True
            choice = False
            servantTarget = ""
            for servant in ennemy["field"]:
                if servant["name"] == nameServantTarget:
                    servantTarget = servant
            print("-----------FIGHT-----------")
            print(servantAttack["name"], " (", servantAttack["attack"], "/", servantAttack["health"], ") attaque ", servantTarget["name"], " (", servantTarget["attack"], "/", servantTarget["health"], ")")
            fight(servantAttack, servantTarget)

#Nettoie le champ de bataille

            if(servantTarget["health"] <= 0) :
                 ennemy["field"].remove(servantTarget)
                 print( servantTarget["name"], " est hors jeu")
            else :
                print("Il reste ",  servantTarget["health"], " points de vie a ", servantTarget["name"])

#Phase d'envoie sur le champ de bataille


    print("Liste de vos serviteur dans votre main")
    for cardPlayer in player["hand"] :
        printCard(cardPlayer)
    if len(player["hand"]) > 0 :
        print("Quel serviteur voulez vous envoyer sur le terrain ?")
        nameServantGoToField = ""
        while (choice == False) :
             nameServantGoToField = input("Choisisez le nom du serviteur a envoyer")
             for card in player["hand"] :
                if nameServantGoToField == card["name"] :
                    choice = True
        for servant in player["hand"]:
            if servant["name"] == nameServantGoToField:
                player["field"].append(servant)
                player["hand"].remove(servant)
    servantCanAttack = list(player["field"])

    pass


if __name__ == '__main__':
    main()