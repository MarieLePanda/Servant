#-------------------------------------------------------------------------------
# Name:        Power
# Purpose:
#
# Author:      lug13995
#
# Created:     02/06/2014
# Copyright:   (c) lug13995 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#from Player import Player

class Power :

    def __init__(self, name, value) :
        self.name = name
        self.value = value

    def invokServant(player) :
        player.pickUp(player.deck)


    def attackServant(player, enemy, card) :
        if card.power.name == "AttaqueSolo" :
            print(card.name, " peut attaquer")

    def attackServantMultiple(enemy, card) :
        if card.power.name == "AttaqueMultiple" :
            print(card.name, " inflige des degat a tous les ennemies")
            for cardEnemy in enemy.field :
                print(cardEnemy.name, " Prend ", card.power.value, " de degat")
                if cardEnemy.shield > 0 :
                    cardEnemy.shield -= card.power.value
                else :
                     cardEnemy.health -= card.power.value
                if cardEnemy.shield > 0 :
                    cardEnemy.health += card.power.value
                    cardEnemy.shield = 0
                if cardEnemy.health <= 0 :
                    print(cardEnemy.name, " est hors jeu")
                else :
                    print("Il reste ", cardEnemy.health, " pv a ", cardEnemy.name)



    def addHpMax(player, card) :
        print("Un servant augmente ses pv max")


    def addHpMaxMultiple(player, card) :
        print("plusieurs servant augmentent leur pv max")


    def addHp(player, card) :
        print("Un servant regagne des pv")


    def addHpMultiple(player, card) :
        print("Plusieur servant regagnent des pv")


    def newPropritie(player, card) :
        print("Un servant à une nouvelle propriete")


    def losePropritie(player, card) :
        print("Un servant perd un propriete")


    def pickupCard(player) :
        print("Un joueur pioche une carte")


    def dropCard(player) :
        print("Un joueur defause une carte")