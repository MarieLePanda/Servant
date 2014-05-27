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

class CardSet :

    listCard = []

    def loadCardSet(nameFile) :
        """Load a card set from a file"""

        file = open(nameFile)
        listServant = []
        for line in file:
            cardSet = []
            for word in line.split():
                if word.isnumeric():
                    cardSet.append(int (word))
                else:
                    cardSet.append(word)
            listServant.append(Card(cardSet[0], cardSet[2], cardSet[1], cardSet[3], cardSet[4], cardSet[5], cardSet[6], cardSet[7]))
        file.close
        CardSet.listCard = listServant

