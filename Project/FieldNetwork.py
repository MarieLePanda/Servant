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
from Card import Card
from Player import Player
from CardSet import CardSet

class FieldNetwork :

    def playTrun(player, enemy, connectionClient) :
        """The player can send a servant in the field and attack the enemy player or servants"""

        connectionClient.send(player.name.encode())
        print("=======================DEBUT PHASE DE JEU JOUEUR ", player.name ,"=======================")
        choice = False
        winner = None
        listCard = CardSet.loadCardSet("C:\\Users\\MKSJ\\Documents\\GitHub\\Servant\\Exo 2\\cardSet")
        playerOne = Player("panda", listCard)
        print("connection faite")
        msgClient = b""
        player.toString()

    #Test si le joueur peut attaquer

        if len(player.field) <= 0 :
            print("\nVous n'avez aucun serviteur pour attaquer")
        else :

    #Phase d'attaque

            servantCanAttack = list(player.field)
            while 0 < len(servantCanAttack) :
                player.displayField(enemy)
                print("\nAvec quel serviteur voulez vous attaquer ?")
                nameServantAttack = ""

        #Selection du serviteur d'attaque

                servantAttack = player.selectedStricker(servantCanAttack)

        #Selection de la cible
                if 0 < len(enemy.field) :
                    player.displayField(enemy)
                    print("\nVoulez vous attaquer le joueur ennemie ou ses servant ?")
                    target = player.selectedTarget(enemy)
                    if type(target) == Player :
                        servantAttack.newFight(enemy = target)
                    else :
                        servantAttack.newFight(card = target)
                else :
                    print("Vous ne pouvez qu'attaquer le joueur")
                    servantAttack.newFight(enemy)
                player.clean()
                enemy.clean()
                if enemy.health <= 0 :
                    print("VICTOIRE")
                    return player

        player.deploy()
        player.setMana(player.mana + 1)
        #player.pickUp(CardSet.listCard)
        return winner