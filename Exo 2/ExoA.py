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



def loadCard(name, health, attack, cost) :
    """Create servant card"""

    cardServant = {"name" : name, "health" : health, "attack" : attack, "cost" : cost}
    return cardServant



def printCard(servant, displayMana = True) :
    """display servant cards"""

    if(displayMana):
        print("name " , servant["name"] ,
        "(" , servant["attack"] , "/" , servant["health"] , ") : ",
        servant["cost"]
         )
    else:
        print("name " , servant["name"] ,
        "(" , servant["attack"] , "/" , servant["health"] , ")")



def fight(servantOne, servantTwo) :
    """Servant one hit servant two"""

    servantTwo["health"] -= servantOne["attack"]



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




def initPlayer(serviteur):
    """Create player witch a hand of 4 cards"""

    hand = []
    while len(hand) < 4 :
        numCard = random.randint(0, len(serviteur) - 1)
        if(serviteur[numCard] not in hand) :
            hand.append(serviteur[numCard])
            serviteur.remove(serviteur[numCard])
    player = {"health" : 30, "mana" : 1, "hand" : hand, "field" : []}
    return player



def playTrun(player, enemy):
    """The player can send a servant in the field and attack the enemy player or servants"""

    choice = False
    print("================================")
    toStringPlayer(player)

#Test si le joueur peut attaquer

    if len(player["field"]) == 0 :
        print("\nVous n'avez aucun serviteur pour attaquer")
    elif len(enemy["field"] ) == 0 :
        print("Il n'y a aucune serviteur ennemie a attaquer")
    else :

#Phase d'attaque

        servantCanAttack = list(player["field"])
        while 0 < len(servantCanAttack) :
            print("\nAvec quel serviteur voulez vous attaquer ?")
            nameServantAttack = ""

    #Selection du serviteur d'attaque

            servantAttack = selectedStricker(player, servantCanAttack)

    #Selection du serviteur ennemie cible

            servantTarget = selectedTarget(enemy)

            print("\n-----------FIGHT-----------\n")
            print(servantAttack["name"], " (", servantAttack["attack"], "/", servantAttack["health"], ") attaque ", servantTarget["name"], " (", servantTarget["attack"], "/", servantTarget["health"], ")")
            fight(servantAttack, servantTarget)

    #Nettoyage le champ de bataille

            if(servantTarget["health"] <= 0) :
                 enemy["field"].remove(servantTarget)
                 print( servantTarget["name"], " est hors jeu")
            else :
                print("Il reste ",  servantTarget["health"], " points de vie a ", servantTarget["name"])

#Phase d'envoie sur le champ de bataille

    goToTheField(player)
    servantCanAttack = list(player["field"])
    player["mana"] += 1




def selectedStricker(player, servantCanAttack):
    """Returns the servant selected to attack"""

    choice = False
    print("\nListe des servants sur le terrain")
    for cardPlayer in player["field"] :
       printCard(cardPlayer)
    print("\nListe de vos serviteur sur le terrain qui peuvent attaquer")
    for cardPlayer in servantCanAttack :
       printCard(cardPlayer)
    while choice == False :
       nameServantAttack = input("Choisisez le nom du serviteur qui va attaquer\n")
       for card in servantCanAttack :
           if nameServantAttack == card["name"] :
               choice = True
    choice = False
    servantAttack = ""
    for servant in servantCanAttack :
       if servant["name"] == nameServantAttack:
           servantAttack = servant
           servantCanAttack.remove(servant)

    return servantAttack



def selectedTarget(enemy) :
    """Returns the enemy servant targeted for attack"""

    choice = False
    print("\nListe des serviteur adverse sur le terrain")
    for cardPlayer in enemy["field"] :
        printCard(cardPlayer)
    print("\nQuel serviteur ennemie voulez vous attaquer ?")
    nameServantTarget = ""
    while choice == False:
        nameServantTarget = input("Choisisez le nom du serviteur a attaquer\n")
        for card in enemy["field"] :
            if nameServantTarget == card["name"] :
                choice = True
    choice = False
    servantTarget = ""
    for servant in enemy["field"]:
        if servant["name"] == nameServantTarget:
            servantTarget = servant

    return servantTarget


def goToTheField(player) :
    """Sends a servant on the field"""

    choice = False
    print("\nListe de vos serviteur dans votre main")
    for cardPlayer in player["hand"] :
        printCard(cardPlayer)
    if len(player["hand"]) > 0 :
        print("\nQuel serviteur voulez vous envoyer sur le terrain ?")
        nameServantGoToField = ""
        while (choice == False) :
             nameServantGoToField = input("Choisisez le nom du serviteur a envoyer\n")
             for card in player["hand"] :
                if nameServantGoToField == card["name"] :
                    choice = True
        for servant in player["hand"]:
            if servant["name"] == nameServantGoToField:
                player["field"].append(servant)
                player["hand"].remove(servant)



def toStringPlayer(player) :
    """Displays health and mana player"""

    print("Player - health : ", player["health"], " Mana : ", player["mana"] )




if __name__ == '__main__':
    main()