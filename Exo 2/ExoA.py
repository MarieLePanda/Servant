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
    playerOne = initPlayer("Panda", cardSet)
    playerTwo = initPlayer("Koala", cardSet)
    playerWinner = None
    i = 0
    while playerWinner == None :
        if i % 2 == 0 :
            playerWinner = playTrun(playerOne, playerTwo)
        else :
            playerWinner = playTrun(playerTwo, playerOne)
        i += 1
    print("==================================")
    print("\nLe gagnant est ", playerWinner["name"], " avec ", playerWinner["health"], " pv restant")


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

    print("\n-----------FIGHT-----------\n")
    print(servantOne["name"], " (", servantOne["attack"], "/", servantOne["health"], ") attaque ", servantTwo["name"], " (", servantTwo["attack"], "/", servantTwo["health"], ")")
    servantTwo["health"] -= servantOne["attack"]


def newFight(servantOne, enemy = None, servantTwo = None):

    print("\n-----------FIGHT-----------\n")
    if enemy == None :
        print(servantOne["name"], " (", servantOne["attack"], "/", servantOne["health"], ") attaque ", servantTwo["name"], " (", servantTwo["attack"], "/", servantTwo["health"], ")")
        servantTwo["health"] -= servantOne["attack"]
    else :
        print(servantOne["name"], " (", servantOne["attack"], "/", servantOne["health"], ") attaque ", enemy["name"], " (", enemy["health"], ")")
        enemy["health"] -= servantOne["attack"]

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




def initPlayer(namePlayer, serviteur):
    """Create player witch a hand of 4 cards"""

    hand = []
    while len(hand) < 4 :
        numCard = random.randint(0, len(serviteur) - 1)
        if(serviteur[numCard] not in hand) :
            hand.append(serviteur[numCard])
            serviteur.remove(serviteur[numCard])
    player = {"name" : namePlayer, "health" : 30, "mana" : 1, "hand" : hand, "field" : []}
    return player



def playTrun(player, enemy):
    """The player can send a servant in the field and attack the enemy player or servants"""

    print("=======================DEBUT PHASE DE JEU JOUEUR ", player["name"] ,"=======================")
    choice = False
    toStringPlayer(player)

#Test si le joueur peut attaquer

    if len(player["field"]) == 0 :
        displayField(player, enemy)
        print("\nVous n'avez aucun serviteur pour attaquer")
    else :

#Phase d'attaque

        servantCanAttack = list(player["field"])
        while 0 < len(servantCanAttack) :
            displayField(player, enemy)
            print("\nAvec quel serviteur voulez vous attaquer ?")
            nameServantAttack = ""

    #Selection du serviteur d'attaque

            servantAttack = selectedStricker(player, servantCanAttack)

    #Selection de la cible
            if 0 < len(enemy["field"]) :
                displayField(player, enemy)
                print("\nVoulez vous attaquer le joueur ennemie ou ses servant ?")
                choice = False
                while choice == False :
                    target = input("Joueur ou servant ?\n").lower()
                    if target =="joueur" :
                        choice = True
                        newFight(servantAttack, enemy)
                        if(enemy["health"] <= 0) :
                            print( enemy["name"], " est hors jeu")
                            return player
                        else :
                            print("Il reste ",  enemy["health"], " points de vie a ", enemy["name"])
                    elif target =="servant" :
                        choice = True
                        servantTarget = selectedTarget(enemy)
                        newFight(servantAttack, servantTarget)
                        if(servantTarget["health"] <= 0) :
                            print( servantTarget["name"], " est hors jeu")
                            enemy["field"].remove(servantTarget)
                        else :
                            print("Il reste ",  servantTarget["health"], " points de vie a ", servantTarget["name"])
            else :
                newFight(servantAttack, enemy)
                if(enemy["health"] <= 0) :
                    print( servantTarget["name"], " est hors jeu")
                    return player
                else :
                    print("Il reste ",  enemy["health"], " points de vie a ", enemy["name"])


    #Nettoyage le champ de bataille


#Phase d'envoie sur le champ de bataille

    goToTheField(player)
    servantCanAttack = list(player["field"])
    player["mana"] += 1
    return None




def selectedStricker(player, servantCanAttack):
    """Returns the servant selected to attack"""

    print("=======================DEBUT PHASE SELECTION ATTAQUANT=======================")
    choice = False
    print("\nListe des servants sur le terrain")
    for cardPlayer in player["field"] :
       printCard(cardPlayer)
    print("\nListe de vos serviteur sur le terrain qui peuvent attaquer")
    for cardPlayer in servantCanAttack :
       printCard(cardPlayer)
    while choice == False :
       nameServantAttack = input("Choisisez le nom du serviteur qui va attaquer\n").lower()
       for card in servantCanAttack :
           if nameServantAttack == card["name"].lower() :
               choice = True
               servantAttack = card
               servantCanAttack.remove(card)
    print("=======================FIN PHASE SELECTION ATTAQUANT=======================")

    return servantAttack



def selectedTarget(enemy) :
    """Returns the enemy servant targeted for attack"""

    print("=======================DEBUT PHASE SELECTION CIBLE=======================")
    choice = False
    print("\nListe des serviteur adverse sur le terrain")
    for cardPlayer in enemy["field"] :
        printCard(cardPlayer)
    print("\nQuel serviteur ennemie voulez vous attaquer ?")
    nameServantTarget = ""
    while choice == False:
        nameServantTarget = input("Choisisez le nom du serviteur a attaquer\n").lower()
        for card in enemy["field"] :
            if nameServantTarget == card["name"].lower() :
                choice = True
                servantTarget = card
    choice = False
    print("=======================DEBUT PHASE SELECTION CIBLE=======================")

    return servantTarget


def goToTheField(player) :
    """Sends a servant on the field"""

    print("=======================DEBUT PHASE ENVOIE SUR TERRAIN=======================")
    choice = False
    print("\nListe de vos serviteur dans votre main")
    for cardPlayer in player["hand"] :
        printCard(cardPlayer)
    if len(player["hand"]) > 0 :
        print("\nQuel serviteur voulez vous envoyer sur le terrain ?")
        nameServantGoToField = ""
        while (choice == False) :
            toStringPlayer(player)
            nameServantGoToField = input("Choisisez le nom du serviteur a envoyer ou 0 si vous ne voulez envoyer personne\n").lower()
            for card in player["hand"] :
                if nameServantGoToField == card["name"].lower():
                    resMana = enoughMana(player, card)
                    if resMana == True :
                        choice = True
                        player["field"].append(card)
                        player["hand"].remove(card)
                elif nameServantGoToField == "0" :
                    choice = True
    print("=======================FIN PHASE ENVOIE SUR TERRAIN=======================")



def toStringPlayer(player) :
    """Displays health and mana player"""

    print("Player - health : ", player["health"], " Mana : ", player["mana"] )


def enoughMana(player, servant) :
    res = False
    if servant["cost"] <= player["mana"] :
        res = True
        player["mana"] -= servant["cost"]
        print(servant["name"], " envoye sur le terrain")
        print("Il vous reste ", player["mana"], " de mana")
    else :
        print("Vous n'avez pas assez de mana pour choisir cette carte")

    return res


def displayField(player, enemy) :
    print("------------------------------------")
    print("\nServiteur sur le terrain")
    print(player["name"], " :", player["health"])
    for cardPlayer in player["field"] :
        printCard(cardPlayer)
    print(enemy["name"], " :", enemy["health"])
    for cardPlayer in enemy["field"] :
        printCard(cardPlayer)
    print("------------------------------------")

if __name__ == '__main__':
    main()