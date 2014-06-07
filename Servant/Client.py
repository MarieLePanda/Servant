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

import socket
import sys
import time

from Card import Card
from Player import Player
from CardSet import CardSet
from Field import Field

def main():

    CardSet.loadCardSet("CardSet")
    playerOne = Player("koala", CardSet.listCard)
    playerTwo = Player("panda", CardSet.listCard)
    print(sys.version)
    i = 1
    winner = None
    while winner == None :
        if i % 2 == 0 :
            winner = Field.playTurn(playerOne, playerTwo)
        else :
            winner = Field.playTurn(playerTwo, playerOne)
        i += 1
    playerOne.toString()
    playerTwo.toString()
    print("Vainqueur : ", winner.name)




if __name__ == '__main__':
    main()