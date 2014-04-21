#-------------------------------------------------------------------------------
# Name:        Card
# Purpose:
#
# Author:      MKSJ
#
# Created:     20/04/2014
# Copyright:   (c) MKSJ 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Card :

    def __init__(self, name, health, attack, cost) :
        """Create card"""

        self.name = name
        self.health = health
        self.attack = attack
        self.cost = cost



    def print(self, displayMana = True) :
        """Display card"""

        if(displayMana):
            print(self.name ,  "(" , self.attack , "/" , self.health , ") : ", self.cost)
        else:
            print(self.name , "(" , self.attack , "/" , self.health , ")")



    def fight(self, card) :
        """Servant one hit servant two"""

        print("\n-----------FIGHT-----------\n")
        print(self.name, " (", self.attack, "/", self.health, ") attaque ", card.name, " (", card.attack, "/", card.health, ")")
        card.health -= self.attack
        self.health -= card.attack



    def newFight(self, enemy = None, card = None):
        """Servant one hit enemy or servant card"""

        print("\n-----------FIGHT-----------\n")
        if enemy == None :
            print(self.name, " (", self.attack, "/", self.health, ") attaque ", card.name, " (", card.attack, "/", card.health, ")")
            card.health -= self.attack
            self.health -= card.attack
            if self.health <= 0 :
                print(self.name, " est hors jeu")
            else :
                print("Il reste ", self.health, " pv a ", self.name)
            if card.health <= 0 :
                print(card.name, " est hors jeu")
            else :
                print("Il reste ", card.health, " pv a ", card.name)
        else :
            print(self.name, " (", self.attack, "/", self.health, ") attaque ", enemy.name, " (", enemy.health, ")")
            enemy.health -= self.attack
            if self.health <= 0 :
                print(self.name, " est hors jeu")
            else :
                print("Il reste ", self.health, " pv a ", self.name)
            if enemy.health <= 0 :
                print(enemy.name, " est hors jeu")
            else :
                print("Il reste ", enemy.health, " pv a ", enemy.name)




    def isAlive(self) :
        """Check if servant is always live"""

        return self.health > 0

