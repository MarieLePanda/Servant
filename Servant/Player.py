#-------------------------------------------------------------------------------
# Name:        Player
# Purpose:
#
# Author:      MKSJ
#
# Created:     20/04/2014
# Copyright:   (c) MKSJ 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import time
from Power import Power


class Player :

    def __init__(self, name, deck) :
        """Create player"""

        self.hand = []
        self.deck = deck
        while len(self.hand) < 4 :
            numCard = random.randint(0, len(self.deck) - 1)
            self.hand.append(self.deck[numCard])
            self.deck.remove(self.deck[numCard])
        self.name = name
        self.health = 3
        self.mana = 1
        self.field = []
        self.provocField = []
        self.camoField = []



    def setMana(self, mana) :
        """Change value of mana"""
        self.mana = mana



    def pickUp(self, listCard) :
        """add card in hand"""

        print(self.name, " pioche une carte")
        numCard = random.randint(0, len(listCard) - 1)
        listCard[numCard].print()
        self.hand.append(listCard[numCard])
        listCard.remove(listCard[numCard])



    def deploy(self, enemy) :
        """Sends a servant on the field"""

        print("=======================DEBUT PHASE ENVOIE SUR TERRAIN=======================")
        time.sleep(2)
        self.toString()
        time.sleep(2)
        choice = False
        print("\nListe de vos serviteur dans votre main")
        for cardPlayer in self.hand :
            cardPlayer.print()
            time.sleep(1)
        time.sleep(2)
        if len(self.hand) > 0 :
            print("\nQuel serviteur voulez vous envoyer sur le terrain ?")
            nameServantGoToField = ""
            while (choice == False) :
                nameServantGoToField = input("Choisisez le nom du serviteur a envoyer ou 0 si vous ne voulez envoyer personne\n").lower()
                for card in self.hand :
                    if nameServantGoToField == card.name.lower() and card.cost <= self.mana:
                        choice = True
                        self.field.append(card)
                        self.hand.remove(card)
                        self.setMana(self.mana - card.cost)
                        Power.attackServant(self, enemy, card)
                        Power.attackServantMultiple(enemy, card)
                        Power.addHpMax(self, enemy, card)
                        Power.addHpMaxMultiple(self, enemy, card)
                        Power.pickupCard(self, cardPlayer)
                    elif nameServantGoToField == "0" :
                        choice = True
            
        else :
            print("Vous n'avez aucune carte dans votre main")
        time.sleep(2)            
        print("=======================FIN PHASE ENVOIE SUR TERRAIN=======================")
        time.sleep(2)



    def clean(self) :
        """clean field"""
        for card in self.field :
            if card.isAlive() == False :
                self.field.remove(card)


    def toString(self) :
        """Displays health and mana player"""

        print("Player ", self.name, " - health : ", self.health, " Mana : ", self.mana )


    def displayField(self, enemy) :
        """Display all card in the field"""
        print("------------------------------------")
        print("\nServiteur sur le terrain")
        print(self.name, " :", self.health)
        for cardPlayer in self.field :
            cardPlayer.print()
            time.sleep(1)
        print(enemy.name, " :", enemy.health)
        for cardEnemy in enemy.field :
            cardEnemy.print(False)
            time.sleep(1)
        print("------------------------------------")



    def selectedStricker(self, servantCanAttack):
        """Returns the servant selected to attack"""

        print("=======================DEBUT PHASE SELECTION ATTAQUANT=======================")
        time.sleep(2)
        choice = False
        print("\nListe des servants sur le terrain")
        for cardPlayer in self.field :
            cardPlayer.print(False)
            time.sleep(1)
        time.sleep(2)

        print("\nListe de vos serviteur sur le terrain qui peuvent attaquer")
        for cardPlayer in servantCanAttack :
            cardPlayer.print(False)
            time.sleep(1)
        time.sleep(2)
        while choice == False :
            nameServantAttack = input("Choisisez le nom du serviteur qui va attaquer\n").lower()
            for cardPlayer in servantCanAttack :
                if nameServantAttack == cardPlayer.name.lower() :
                    choice = True
                    cardPlayer.camo = "Nocamo"
                    servantAttack = cardPlayer
                    servantCanAttack.remove(cardPlayer)
        print("=======================FIN PHASE SELECTION ATTAQUANT=======================")
        time.sleep(2)

        return servantAttack



    def selectedTarget(self, enemy) :
        """Returns the enemy servant targeted for attack"""

        print("=======================DEBUT PHASE SELECTION CIBLE=======================")
        time.sleep(2)
        print("\nListe des serviteur adverse sur le terrain")
        for cardEnemy in enemy.field :
            if cardEnemy not in enemy.camoField :
                cardEnemy.print(False)
                time.sleep(1)
        time.sleep(2)
        if len(enemy.provocField) > 0:
            print("Les serviteur ennemie vous provoque\n")
            return self.choseProvocServant(enemy)
        else:
            return self.chosePlayerOrServant(enemy)

        print("=======================FIN PHASE SELECTION CIBLE=======================")
        time.sleep(2)


    def chosePlayerOrServant(self, enemy, power = False):
        print("\nVoulez vous attaquer le joueur ennemie ou ses serviteurs ?")
        while True :
            if power == False :
                target = input("Joueur ou serviteur ?\n").lower()
                if target == "joueur" :
                    #choiceTarget = True
                    return enemy
                elif target == "serviteur" :
                    #choiceTarget = True
                    print("\nQuel serviteur ennemie voulez vous attaquer ?")
                    nameServantTarget = ""
                    while True:
                        nameServantTarget = input("Choisisez le nom du serviteur a attaquer\n").lower()
                        for cardEnemy in enemy.field :
                            if nameServantTarget == cardEnemy.name.lower() and cardEnemy not in enemy.camoField :
                                return cardEnemy
            else :
                print("\nQuel serviteur ennemie voulez vous attaquer ?")
                nameServantTarget = ""
                while True:
                    nameServantTarget = input("Choisisez le nom du serviteur a attaquer\n").lower()
                    for cardEnemy in enemy.field :
                        if nameServantTarget == cardEnemy.name.lower() and cardEnemy not in enemy.camoField :
                            return cardEnemy



    def choseProvocServant(self, enemy):
        while True:
            for cardEnemy in enemy.provocField :
                cardEnemy.print(False)
                time.sleep(1)
            time.sleep(2)
            nameServantTarget = input("Choisisez le nom du serviteur a attaquer\n").lower()
            for cardEnemy in enemy.provocField :
                if nameServantTarget == cardEnemy.name.lower() :
                    return cardEnemy