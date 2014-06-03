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

        self.name = name
        self.health = health
        self.attack = attack
        self.cost = cost


    def printCard(displayMana = True) :

        if(displayMana):
            print("name " , name ,  "(" , attack , "/" , health , ") : ", cost)
        else:
            print("name " , servant["name"] , "(" , servant["attack"] , "/" , servant["health"] , ")")
