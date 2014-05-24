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

    def __init__(self, name, health, attack, cost, provoc, shield, camo) :
        """Create card"""

        self.name = name
        self.health = health
        self.attack = attack
        self.cost = cost
        self.provoc = provoc
        self.shield = shield
        self.camo = camo

    def print(self, displayMana = True) :
        """Display card"""

        if(displayMana):
            print(self.name ,  "( Attaque : " , self.attack , "Santé : " , self.health , "/ bouclier : ", self.shield, ") Mana : ", self.cost, self.isProvoc(), self.isCamo())
        else:
            print(self.name ,  "( Attaque : " , self.attack , "Santé : " , self.health , "/ bouclier : ", self.shield, ")", self.isProvoc(), self.isCamo())



    def fight(self, card) :
        """Servant one hit servant two and servant two against attack"""

        print("\n-----------FIGHT-----------\n")
        print(self.name, " (", self.attack, "/", self.health, ") attaque ", card.name, " (", card.attack, "/", card.health, ")")
        if card.shield > 0 :
            card.shield -= self.attack
        else :
             card.health += self.attack
        if card.shield > 0 :
            card.health += card.shield
            card.shield = 0

        if self.shield > 0 :
            self.shield -= card.attack
        else :
             self.health += card.attack
        if self.shield > 0 :
            self.health += self.shield
            self.shield = 0



    def newFight(self, enemy = None, card = None):
        """Servant one hit enemy or servant card"""

        print("\n-----------FIGHT-----------\n")
        if enemy == None :
            print(self.name, " (", self.attack, "/", self.health, ") attaque ", card.name, " (", card.attack, "/", card.health, ")")
            if card.shield > 0 :
                print("Le bouclier de ",  card.name, " absorde les dégats")
                card.shield -= self.attack
            else :
                 card.health += self.attack
            if card.shield < 0 :
                print("Le bouclier de ", card.name,"à cédé")
                card.health += card.shield
                card.shield = 0

            if self.shield > 0 :
                print("Le bouclier de ",  self.name, " absorde les dégats")
                self.shield -= card.attack
            else :
                 self.health += card.attack

            if self.shield < 0 :
                print("Le bouclier de ",  self.name,"à cédé")
                self.health += self.shield
                self.shield = 0

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

    def isProvoc(self) :
        if self.provoc == "Provoc":
            return"provoc : activé"
        else :
            return "provoc : non activé"

    def isCamo(self) :
        if self.camo == "Camo":
            return" | est camouflé"
        else :
            return " | n'est pas camouflé"