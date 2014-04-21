#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lug13995
#
# Created:     18/04/2014
# Copyright:   (c) lug13995 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import socket
from Card import Card
from Player import Player
from CardSet import CardSet


def main():

    connectionServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connectionServeur.connect(("localhost", 12800))
    listCard = CardSet.loadCardSet("C:\\Users\\MKSJ\\Documents\\GitHub\\Servant\\Exo 2\\cardSet")
    print("Connexion reussite avec le serveur")
    msgServeur = b""
    while msgServeur != b"fin":
        msgServeur = input("> ")
        # Peut planter si vous tapez des caractères spéciaux
        msgServeur = msgServeur.encode()
        # On envoie le message
        connectionServeur.send(msgServeur)
        msg_recu = connectionServeur.recv(1024)
        print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents






def playTrun(player, enemy):
    """The player can send a servant in the field and attack the enemy player or servants"""

    print("=======================DEBUT PHASE DE JEU JOUEUR ", player.name ,"=======================")
    choice = False
    winner = None
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
    player.pickUp(CardSet.listCard)
    return winner


if __name__ == '__main__':
    main()