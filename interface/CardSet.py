#-------------------------------------------------------------------------------
# Name:        CardSet
# Purpose:
#
# Author:      MKSJ
#
# Created:     20/04/2014
# Copyright:   (c) MKSJ 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Card import Card
from Player import Player
from Power import Power
import pygame
from pygame.locals import *


class CardSet :

    listCard = []

    def loadCardSet(nameFile) :
        """Load a card set from a file"""

        file = open(nameFile)
        listServant = []
        listServantG = []
        for line in file:
            cardSet = []
            for word in line.split():
                if word.isnumeric():
                    cardSet.append(int (word))
                else:
                    cardSet.append(word)
            #listServant.append(Card(cardSet[0], cardSet[2], cardSet[1], cardSet[3], cardSet[4], cardSet[5], cardSet[6], cardSet[7],
            #                        Power(cardSet[8], cardSet[9])
            #                        ))
            listServantG.append(Card({"carte" : pygame.image.load(str(cardSet[0]) + ".png").convert_alpha(),"name": cardSet[0], "attack" : cardSet[1],"cost" : cardSet[2] , "health" : cardSet[3], "attackImg" : pygame.image.load(str(cardSet[1]) + ".png").convert_alpha(), "healthImg" : pygame.image.load(str(cardSet[3]) + ".png").convert_alpha(), "provoc" : cardSet[4], "shield" : cardSet[5] , "camo" : cardSet[6], "element" : cardSet[7], "power" : Power(cardSet[8], cardSet[9]), "posx" : 0, "posy" : 0, "attackPosx" : 0, "attackPosy" : 0, "healthPosx" : 0, "healthPosy" : 0, "shieldPosx" : 0, "shieldPosy" : 0, "statu" : 1}))
        file.close
        #CardSet.listCard = listServant
        CardSet.listCardG = listServantG


