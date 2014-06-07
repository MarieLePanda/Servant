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
import time

class Power :

    def __init__(self, name, value) :
        
        self.name = name
        self.value = value

    def invokServant(player, enemy, card) :
        
        if card.power.name == "Invoquation" :
            print(player.name, " Peux invoquer un serviteur")
            player.deploy(enemy)


    def attackServant(player, enemy, card) :
        
        if card.power.name == "AttaqueSolo" :
            print(card.name, " peut attaquer")
            
            if 0 < len(enemy.field) and len(enemy.field) > len(enemy.camoField) :
                player.displayField(enemy)
                cardEnemy = player.chosePlayerOrServant(enemy, True)
                print(cardEnemy.name, " Prend ", card.power.value, " de degat")
                if cardEnemy.shield > 0 :
                    cardEnemy.shield -= card.power.value
                else :
                    cardEnemy.health -= card.power.value
                if cardEnemy.shield < 0 :
                    cardEnemy.health += card.power.value
                    cardEnemy.shield = 0
                if cardEnemy.health <= 0 :
                    print(cardEnemy.name, " est hors jeu")
                    Power.invokServant(enemy, player, cardEnemy)
                else :
                    print("Il reste ", cardEnemy.health, " pv a ", cardEnemy.name)
            else :
                print("Personne a attaquer")


    def attackServantMultiple(enemy, card) :
        
        if card.power.name == "AttaqueMultiple" :
            print(card.name, " inflige des degat a tous les ennemies")
            for cardEnemy in enemy.field :
                print(cardEnemy.name, " Prend ", card.power.value, " de degat")
                if cardEnemy.shield > 0 :
                    cardEnemy.shield -= card.power.value
                else :
                    cardEnemy.health -= card.power.value
                if cardEnemy.shield < 0 :
                    cardEnemy.health += card.power.value
                    cardEnemy.shield = 0
                if cardEnemy.health <= 0 :
                    print(cardEnemy.name, " est hors jeu")
                else :
                    print("Il reste ", cardEnemy.health, " pv a ", cardEnemy.name)



    def addHpMax(player, enemy, card) :
        
        if card.power.name == "AjoutPvSolo" :
            print(card.name, " peut augmenter la sante max d'un serviteur")
            for cardPlayer in player.field :
                cardPlayer.print(False)
                time.sleep(1)
            time.sleep(2)
            while(True) :
                nameServantTarget = input("Choisisez le nom du serviteur a booster\n").lower()
                for cardPlayer in player.field :
                    if nameServantTarget == cardPlayer.name.lower() :
                        cardPlayer.healthMax += card.power.value
                        print(cardPlayer.name, " a vu sa sante augmente")
                        return


    def addHpMaxMultiple(player, enemy, card) :
        print("plusieurs servant augmentent leur pv max")


    def addHp(player, enemy, card) :
        print("Un servant regagne des pv")


    def addHpMultiple(player, enemy, card) :
        print("Plusieur servant regagnent des pv")


#A placer encore
    def newPropritie(player, card) :
        print("Un servant à une nouvelle propriete")


    def losePropritie(player, card) :
        print("Un servant perd un propriete")


    def pickupCard(player) :
        print("Un joueur pioche une carte")


    def dropCard(player) :
        print("Un joueur defause une carte")