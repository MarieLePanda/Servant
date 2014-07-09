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
#import time
import random

class Power :

    def __init__(self, name, value) :
        
        self.name = name
        self.value = value

    def invokServant(player, enemy, card) :
        
        if card.power.name == "Invoquation" :
            print(player.name, " Peux invoquer un serviteur")
            numCard = random.randint(0, len(player.deck) - 1)
            player.hand.append(player.deck[numCard])
            player.deck.remove(player.deck[numCard])
            player.deploy(enemy, player.hand[-1])


    def attackServant(player, enemy, card) :
        
        if card.power.name == "AttaqueSolo" :
            print(card.name, " peut attaquer")
            
            if 0 < len(enemy.field) and len(enemy.field) > len(enemy.camoField) :
                #player.displayField(enemy)
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
                    if cardEnemy in enemy.field :
                        enemy.field.remove(cardEnemy)
                #else :
                    #print("Il reste ", cardEnemy.health, " pv a ", cardEnemy.name)



    def addHpMax(player, enemy, card) :
        
        if card.power.name == "AjoutPvSolo" :
            print(card.name, " peut augmenter la sante max d'un serviteur")
            for cardPlayer in player.field :
                cardPlayer.print(False)
                #time.sleep(1)
            #time.sleep(2)
            while(True) :
                if player.IAorNot is False:
                    nameServantTarget = input("Choisisez le nom du serviteur a booster\n").lower()
                else :
                    numCard = random.randint(0, len(player.field) - 1)
                    randomCard = player.field[numCard]
                    nameServantTarget = randomCard.name.lower()
                for cardPlayer in player.field :
                    if nameServantTarget == cardPlayer.name.lower() :
                        cardPlayer.healthMax += card.power.value
                        print(cardPlayer.name, " a vu sa sante augmente")
                        return


    def addHpMaxMultiple(player, enemy, card) :
      
        if card.power.name == "AjoutPvMultiple" :
            print(card.name, " peut augmenter la sante max de tous les serviteurs")
            for cardPlayer in player.field :
                cardPlayer.print(False)
                #time.sleep(1)
            #time.sleep(2)
            for cardPlayer in player.field :
                cardPlayer.healthMax += card.power.value
                print(cardPlayer.name, " a vu sa sante augmente")



    def addHp(player, enemy, card) :
        if card.power.name == "RedonnePvSolo" :
            print(card.name, " peut soigner un serviteur")
            for cardPlayer in player.field :
                cardPlayer.print(False)
                #time.sleep(1)
            #time.sleep(2)
            while(True) :
                if player.IAorNot is False:
                    nameServantTarget = input("Choisisez le nom du serviteur a soigner\n").lower()
                else :
                    numCard = random.randint(0, len(player.field) - 1)
                    randomCard = player.field[numCard]
                    nameServantTarget = randomCard.name.lower()
                for cardPlayer in player.field :
                    if nameServantTarget == cardPlayer.name.lower() :
                        cardPlayer.health += card.power.value
                        print(cardPlayer.name, " a ete soigne")
                        if cardPlayer.health > cardPlayer.healthMax :
                            cardPlayer.health = cardPlayer.healthMax
                        return


    def addHpMultiple(player, enemy, card) :
        
        if card.power.name == "RedonnePvMultiple" :
            print(card.name, " soigne tous les serviteurs")
            for cardPlayer in player.field :
                cardPlayer.print(False)
                #time.sleep(1)
            #time.sleep(2)
            for cardPlayer in player.field :
                cardPlayer.health += card.power.value
                print(cardPlayer.name, " a ete soigne")
                if cardPlayer.health > cardPlayer.healthMax :
                    cardPlayer.health = cardPlayer.healthMax


#A placer encore
    def newPropritie(player, card) :
        print("Un serviteur gagne une propriete")

#A placer encore
    def losePropritie(player, card) :
        print("Un servant perd un propriete")


    def pickupCard(player, card) :
        if card.power.name == "PiocheCarte" :
            print(card.name, " permet de piocher une carte")
            player.pickUp(player.deck)


    def dropCard(card, player) :
        if card.power.name == "DefauseCarte" :
            player.needDropCard = True