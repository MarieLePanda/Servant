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
from Card import Card
from Player import Player
from CardSet import CardSet


def main():


    listCard = CardSet.loadCardSet("C:\\Users\\MKSJ\\Documents\\GitHub\\Servant\\Exo 2\\cardSet")
    i = 0
    for c in listCard :
        print(i, " ")
        c.print()
        i +=1
    playerOne = Player("panda", listCard)
    playerTwo = Player("koala", listCard)
    i = 0
    winner = None
##    while winner == None :
##        if i % 2 == 0 :
##            winner = playTrun(playerOne, playerTwo)
##        else :
##            winner =  playTrun(playerTwo, playerOne)
##        i += 1
##    playerOne.toString()
##    playerTwo.toString()
##    print("Vainqueur : ", winner.name)

    for c in listCard :
        print(i, " ")
        c.print()
        i +=1






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