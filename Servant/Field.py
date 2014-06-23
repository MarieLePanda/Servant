#-------------------------------------------------------------------------------
# Name:        FieldNework
# Purpose:
#
# Author:      MKSJ
#
# Created:     21/04/2014
# Copyright:   (c) MKSJ 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import socket
import time
from Card import Card
from Player import Player
from CardSet import CardSet
from Power import Power

class Field :

    def playTurn(player, enemy) :
        """The player can send a servant in the field and attack the enemy player or servants"""
        
        if(player.needDropCard) :
            player.dropCard()
        choice = False
        winner = None
        player.toString()
        time.sleep(2)
        enemy.provocField = Field.loadProvocField(enemy)
        enemy.camoField = Field.loadCamoField(enemy)
        for card in player.field:
            if card not in player.camoField :
                card.print()
        time.sleep(2)
        

    #Test si le joueur peut attaquer

        if len(player.field) <= 0 :
            print("\nVous n'avez aucun serviteur pour attaquer")
            time.sleep(2)
        else :

    #Phase d'attaque

            servantCanAttack = list(player.field)
            while 0 < len(servantCanAttack) :
                player.displayField(enemy)
                print("\nAvec quel serviteur voulez vous attaquer ?")
                time.sleep(2)
                nameServantAttack = ""

        #Selection du serviteur d'attaque

                servantAttack = player.selectedStricker(servantCanAttack)

        #Selection de la cible
                if 0 < len(enemy.field) and len(enemy.field) > len(enemy.camoField) :
                    player.displayField(enemy)
                    time.sleep(2)
                    target = player.selectedTarget(enemy)
                    if type(target) == Player :
                        servantAttack.newFight(player, enemy)
                    else :
                        servantAttack.newFight(player, enemy, card = target)
                else :
                    print("Vous ne pouvez qu'attaquer le joueur")
                    time.sleep(2)
                    servantAttack.newFight(player, enemy)
                player.clean()
                enemy.clean()
                if enemy.health <= 0 :
                    print("VICTOIRE")
                    time.sleep(2)
                    return player

        player.deploy(enemy)
        player.setMana(player.mana + 1)
        #Player.pickUp
        player.pickUp(CardSet.listCard)
        return winner

    def loadProvocField(player):
        provocField = []
        for card in player.field:
            if card.provoc == "Provoc":
                provocField.append(card)
        return provocField

    def loadCamoField(player):
        camoField = []
        for card in player.field:
            if card.camo == "Camo":
                camoField.append(card)
        return camoField