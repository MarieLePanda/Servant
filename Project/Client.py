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
    playerOne = Player("koala", listCard)
    i = 1
    winner = None
    while winner == None :
        if i % 2 == 0 :
            winner = youPlay(playerOne, connectionServeur)
        else :
            winner =  playTrun(playerOne, connectionServeur)
        i += 1
    playerOne.toString()
    playerTwo.toString()
    print("Vainqueur : ", winner.name)

    connectionClient.close()
    connection.close()




def playTrun(player, connectionServeur):
    """The player can send a servant in the field and attack the enemy player or servants"""
    playerName = connectionServeur.recv(1024).decode()
    print("=======================DEBUT PHASE DE JEU JOUEUR ", playerName ,"=======================")
    choice = False
    winner = None
    toStringPlayer = connectionServeur.recv(1024).decode()
    print(toStringPlayer)
    print(connectionServeur.recv(1024).decode())
    input()

if __name__ == '__main__':
    main()