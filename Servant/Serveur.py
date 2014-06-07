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
from FieldNetwork import FieldNetwork


def main():
##
##    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##    connection.bind(("", 12800))
##    connection.listen(5)
##    connectionClient, infosConnection = connection.accept()
##    listCard = CardSet.loadCardSet("C:\\Users\\MKSJ\\Documents\\GitHub\\Servant\\Exo 2\\cardSet")
##    playerOne = Player("panda", listCard)
##    print("connection faite")
##    msgClient = b""
##    while msgClient != b"fin":
##        msgClient = connectionClient.recv(1024)
##        # L'instruction ci-dessous peut lever une exception si le message
##        # RÃ©ceptionnÃ© comporte des accents
##        print(msgClient.decode())
##        msgServer = input(">").encode()
##        connectionClient.send(msgServer)


    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind(("", 12800))
    connection.listen(5)
    connectionClient, infosConnection = connection.accept()
    print("connection faite")
    listCard = CardSet.loadCardSet("C:\\Users\\MKSJ\\Documents\\GitHub\\Servant\\Exo 2\\cardSet")
    playerOne = Player("panda", listCard)
    i = 0
    winner = None
    while winner == None :
        if i % 2 == 0 :
            winner = youPlay(playerOne, connectionClient)
        else :
            winner =  FieldNetwork.playTrun(playerTwo, playerOne, connectionClient)
        i += 1
    playerOne.toString()
    playerTwo.toString()
    print("Vainqueur : ", winner.name)

    connectionClient.close()
    connection.close()





def youPlay(player, connectionClient):
    """The player can send a servant in the field and attack the enemy player or servants"""

    connectionClient.send(player.name.encode())
    print("=======================DEBUT PHASE DE JEU JOUEUR ", player.name ,"=======================")
    choice = False
    winner = None
    playerToString = "Player "
    playerToString += player.name
    playerToString += " - health : "
    playerToString += str(player.health)
    playerToString += " Mana : "
    playerToString += str(player.mana)
    connectionClient.send(playerToString.encode())
    print(player.toString())
    if len(player.field) <= 0 :
        print("\nVous n'avez aucun serviteur pour attaquer")
        connectionClient.send(("Aucun serviteur adverse pour attaquer").encode())
    else :
        input()
    input()


if __name__ == '__main__':
    main()