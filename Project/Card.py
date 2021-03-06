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

    def __init__(self, name, health, attack, cost, provoc, shield, camo, element, power) :
        """Create card"""

        self.name = name
        self.health = health
        self.attack = attack
        self.cost = cost
        self.provoc = provoc
        self.shield = shield
        self.camo = camo
        self.element = element
        self.power = power



    def print(self, displayMana = True) :
        """Display card"""

        if(displayMana):
            print(self.name ,  "(", self.element, ") ( Attaque : " , self.attack , "Sante : " , self.health , "/ bouclier : ", self.shield, ") Mana : ",
                    self.cost, "\n", self.isProvoc(), self.isCamo(),
                    " Pouvoir actif : ", self.power.name, " : ", self.power.name)

        else:
            print(self.name , "(", self.element, ") ( Attaque : " , self.attack , "Sante : " , self.health , "/ bouclier : ", self.shield, ")\n",
                    self.isProvoc(), self.isCamo(),
                    " Pouvoir actif : ", self.power.name )



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
                print("Le bouclier de ",  card.name, " absorde les degats")
                card.shield -= self.calcHavoc(card.element)
            else :
                 card.health -= self.calcHavoc(card.element)
            if card.shield < 0 :
                print("Le bouclier de ", card.name,"a cede")
                card.health += card.shield
                card.shield = 0

            if self.shield > 0 :
                print("Le bouclier de ",  self.name, " absorde les degats")
                self.shield -= card.calcHavoc(self.element)
            else :
                 self.health -= card.calcHavoc(self.element)

            if self.shield < 0 :
                print("Le bouclier de ",  self.name,"a  cede")
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
        """Use to display attribute provocation"""
        if self.provoc == "Provoc":
            return"provoc : active"
        else :
            return "provoc : non active"

    def isCamo(self) :
        """Use to display attribute camo"""
        if self.camo == "Camo":
            return" | est camoufle"
        else :
            return " | n'est pas camoufle"

    def calcHavoc(self, elementDefense) :
        """Return the damage inflicted according the elements"""

        if self.element == "Foudre" and elementDefense == "Eau" :
            return self.attack * 2
        elif self.element == "Eau" and elementDefense == "Feu" :
            return self.attack * 2
        elif self.element == "Feu" and elementDefense == "Foudre" :
            return self.attack * 2
        else :
            return self.attack

