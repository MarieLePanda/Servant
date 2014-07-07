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
import sys
import time



from Player import Player
from Power import Power
from CardSet import CardSet
from Field import Field
import pygame
from pygame.locals import *

def main():

    pygame.init()
    screen_size = 1300, 800
    fenetre = pygame.display.set_mode(screen_size)

    # definir tous fonds
    fondEcran = ["salle", "Terrain", "terrain3", "terrain4", "terrain5", "terrain6"]
    #choix aléatoire du fond
    numFond = random.randint(0, len(fondEcran) - 1)
    fond = pygame.image.load(fondEcran[numFond] + ".png").convert_alpha()
    menu_fond = pygame.image.load("fondPython.jpeg").convert()
    fenetre.blit(menu_fond, (0,0))

    carte_hand = 0, 500, 1300, 800


    carte_posx = 200

    fields = []

    eposy = 100
    menus = [
                {"element" : pygame.image.load("bouton_1_vsIA.png").convert_alpha(), "name" : "jouer VS IA", "posx" : 10, "posy" : 100 },
                {"element" : pygame.image.load("pvp.png").convert_alpha(), "name" : "jouer VS joueur", "posx" : 900, "posy" : 100 },
                {"element" : pygame.image.load("bouton_quitter.png").convert_alpha(), "name" : "quitter", "posx" : 30, "posy" : 250 }
            ]

    endOfRound = {"button" : pygame.image.load("endOfRound.png").convert_alpha(), "name" : "yop", "posx" : 1000, "posy" : 350}
    for i, menu in enumerate(menus) :
        menu_size = menu["element"].get_rect()
        menu["posx"] = (screen_size[0] / 2) - (menu_size[2] / 2) 
        menu["posy"] = eposy
        fenetre.blit(menu["element"], (menu["posx"], menu["posy"]))
        eposy += (menu_size[3] / 2) + menu_size[3]

    pygame.display.flip()

    mode_game = 0
    continuer = 1
    continuer_menu = 1
    continuer_game = 1
    saisi_carte = 0
    saisi_attack = 0
    carte_selection_id = 0
    carte_selection = ()
    carte_attack_id = 0
    carte_attack = ()
    deplacement = 5
    positionOk = 0
    pygame.key.set_repeat(400, 30)
    winner = None
    turn = ["one", "two"]


    while continuer : # boucle général
        if continuer_menu == 1:
            fenetre.blit(menu_fond, (0,0))
            for menu in menus :
                fenetre.blit(menu["element"], (menu["posx"], menu["posy"]))

            pygame.display.flip()

        while continuer_menu: # boucle du menu
            for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                if event.type == QUIT: #Si un de ces événements est de type QUIT
                    continuer_game = 0
                    continuer_menu = 0
                    winner = False
                    continuer = 0

                if event.type == KEYDOWN : # lorsqu'on appui sur un touche du clavier

                    if event.key == K_ESCAPE: # esc on quitte le jeu
                        continuer_game = 0
                        continuer_menu = 0
                        winner = False
                        continuer = 0

                if event.type == MOUSEBUTTONUP: 

                    eposx = event.pos[0]
                    eposy = event.pos[1]
                    if event.button == 1 :
                        for menu in menus:
                            menu_size = menu["element"].get_rect()
                            posx, posy = menu["posx"], menu["posy"]
                            if( ( eposx >= posx and eposx <= (menu_size[2] + posx) ) and ( eposy >= posy and eposy <= (menu_size[3] + posy) ) ):
                                if menu["name"] == "jouer VS IA" :
                                    mode_game = 1
                                    continuer_menu = 0
                                    continuer_game = 1
                                    continuer = 1
                                    #initialiser les cartes du joueur 1
                                    CardSet.loadCardSet("cardSet")
                                    playerOne = Player("koala", CardSet.listCardG, False)
                                    #initilaiser les cartes du joueur 2
                                    CardSet.loadCardSet("cardSet2")
                                    playerTwo = Player("panda", CardSet.listCardG, True)
                                    winner = None
                                    t = random.randint(0, len(turn) - 1)
                                    turnIdx = t
                                    i = 0
                                    #fenetre = pygame.display.set_mode(screen_size, FULLSCREEN)

                                if menu["name"] == "jouer VS joueur" :
                                    mode_game = 2
                                    continuer_menu = 0
                                    continuer_game = 1
                                    continuer = 1
                                    #initialiser les cartes du joueur 1
                                    CardSet.loadCardSet("cardSet")
                                    playerOne = Player("koala", CardSet.listCardG, False)
                                    #initilaiser les cartes du joueur 2
                                    CardSet.loadCardSet("cardSet2")
                                    playerTwo = Player("panda", CardSet.listCardG, True)
                                    winner = None
                                    t = random.randint(0, len(turn) - 1)
                                    turnIdx = t
                                    i = 0
                                    #fenetre = pygame.display.set_mode(screen_size, FULLSCREEN)

                                if menu["name"] == "quitter" :
                                    mode_game = 0
                                    continuer_menu = 0
                                    continuer_game = 0
                                    winner = False
                                    continuer = 0

        while winner == None :
            continuer_game = 1

            carte_posx = 400
            for c in playerOne.hand:
                # positionnement des cartes dans la main
                carte_size = c.carte["carte"].get_rect()
                c.carte["posx"] = carte_posx
                carte_posx += (carte_size[2] / 3)
                c.carte["posy"] = screen_size[1] - (carte_size[3] + 20)

            carte_posx = 400
            for c in playerTwo.hand :
                # positionnement des cartes ennemies dans sa main
                c.carte["carte"] = pygame.image.load("carte_dos.png").convert_alpha()
                carte_size = c.carte["carte"].get_rect()
                c.carte["posx"] = carte_posx
                carte_posx += (carte_size[2] / 3)
                c.carte["posy"] = 20

            carte_posx = 100
            for c in playerOne.field :
                c.carte["carte"] = pygame.image.load(str(c.carte["name"]) + "_pose.png").convert_alpha()
                carte_size = c.carte["carte"].get_rect()
                c.carte["posx"] = carte_posx
                carte_posx += carte_size[2] + 5
                c.carte["posy"] = (screen_size[1] / 2) - 5

            carte_posx = 100
            for c in playerTwo.field :
                c.carte["carte"] = pygame.image.load(str(c.carte["name"]) + "_pose.png").convert_alpha()
                carte_size = c.carte["carte"].get_rect()
                c.carte["posx"] = carte_posx
                carte_posx += carte_size[2] + 5
                c.carte["posy"] = (screen_size[1] / 2) - (carte_size[3] + 10)

            lifeBack = pygame.image.load("vie.png").convert_alpha()
            lifeBackEnemy = pygame.image.load("vie.png").convert_alpha()
            if playerOne.health < 0 :
                playerOne.health = 0
            if playerTwo.health < 0 :
                playerTwo.health = 0
            life = pygame.image.load(str(playerOne.health) + ".png").convert_alpha()
            lifeEnemy = pygame.image.load(str(playerTwo.health) + ".png").convert_alpha()
            fenetre.blit(lifeBackEnemy, (0, 0))
            while continuer_game: # boucle du jeu

                fenetre.blit(fond, (0, 0))
                for c in playerOne.hand:
                    # positionnement des cartes dans la main
                    if c.carte["health"] <= 0 :
                        playerOne.field.remove(c)
                    fenetre.blit(c.carte["carte"], (c.carte["posx"], c.carte["posy"]))
                    carte_size = c.carte["carte"].get_rect()
                    c.carte["attackImg"] = pygame.image.load(str(c.attack) + ".png").convert_alpha()
                    c.carte["healthImg"] = pygame.image.load(str(c.health) + ".png").convert_alpha()
                    c.carte["attackPosx"] = c.carte["posx"] + (carte_size[2] / 15)
                    c.carte["attackPosy"] = c.carte["posy"] + (carte_size[3] - (carte_size[3] / 9))
                    c.carte["healthPosx"] = c.carte["posx"] + (carte_size[2] - (carte_size[2] / 5))
                    c.carte["healthPosy"] = c.carte["posy"] + (carte_size[3] - (carte_size[3] / 9))
                    manax = c.carte["posx"] + 5
                    manay = c.carte["posy"] + 10
                    fenetre.blit(c.carte["attackImg"], (c.carte["attackPosx"], c.carte["attackPosy"]))
                    fenetre.blit(c.carte["healthImg"], (c.carte["healthPosx"], c.carte["healthPosy"]))
                    fenetre.blit(pygame.image.load(str(c.carte["cost"]) + ".png").convert_alpha(), (manax, manay))

                for c in playerTwo.hand:
                    # positionnement des cartes dans la main
                    fenetre.blit(c.carte["carte"], (c.carte["posx"], c.carte["posy"]))

                fenetre.blit(endOfRound["button"], (endOfRound["posx"], endOfRound["posy"]))

                for c in playerOne.field:
                    # positionnement des cartes sur le térrain
                    if c.carte["health"] <= 0 :
                        playerOne.field.remove(c)
                    carte_size = c.carte["carte"].get_rect()
                    fenetre.blit(c.carte["carte"], (c.carte["posx"], c.carte["posy"]))
                    c.carte["attackImg"] = pygame.image.load(str(c.carte["attack"]) + ".png").convert_alpha()
                    c.carte["healthImg"] = pygame.image.load(str(c.carte["health"]) + ".png").convert_alpha()
                    if c.carte["provoc"] == "Provoc" :
                        c.carte["attackPosx"] = c.carte["posx"] + 10
                        c.carte["attackPosy"] = c.carte["posy"] + (carte_size[3] / 2) + 20
                        c.carte["healthPosx"] = c.carte["posx"] + (carte_size[2] - (carte_size[2] / 5)) - 10
                        c.carte["healthPosy"] = c.carte["posy"] + (carte_size[3] / 2) + 20

                    else :
                        c.carte["attackPosx"] = c.carte["posx"] + (carte_size[2] / 15)
                        c.carte["attackPosy"] = c.carte["posy"] + (carte_size[3] - (carte_size[3] / 4))
                        c.carte["healthPosx"] = c.carte["posx"] + (carte_size[2] - (carte_size[2] / 4))
                        c.carte["healthPosy"] = c.carte["posy"] + (carte_size[3] - (carte_size[3] / 4))
                    fenetre.blit(c.carte["attackImg"], (c.carte["attackPosx"], c.carte["attackPosy"]))
                    fenetre.blit(c.carte["healthImg"], (c.carte["healthPosx"], c.carte["healthPosy"]))

                for c in playerTwo.field:
                    # positionnement des cartes sur le térrain
                    if c.carte["health"] <= 0 :
                        playerTwo.field.remove(c)
                    carte_size = c.carte["carte"].get_rect()
                    fenetre.blit(c.carte["carte"], (c.carte["posx"], c.carte["posy"]))
                    c.carte["attackImg"] = pygame.image.load(str(c.carte["attack"]) + ".png").convert_alpha()
                    c.carte["healthImg"] = pygame.image.load(str(c.carte["health"]) + ".png").convert_alpha()
                    c.carte["attackPosx"] = c.carte["posx"] + (carte_size[2] / 15)
                    c.carte["attackPosy"] = c.carte["posy"] + (carte_size[3] - (carte_size[3] / 4))
                    c.carte["healthPosx"] = c.carte["posx"] + (carte_size[2] - (carte_size[2] / 4))
                    c.carte["healthPosy"] = c.carte["posy"] + (carte_size[3] - (carte_size[3] / 4))
                    fenetre.blit(c.carte["attackImg"], (c.carte["attackPosx"], c.carte["attackPosy"]))
                    fenetre.blit(c.carte["healthImg"], (c.carte["healthPosx"], c.carte["healthPosy"]))


                # health player and enemy
                posLifeBack = screen_size[0] - 120, (screen_size[1] - 100)
                posLifeBackEnemy = screen_size[0] - 120, 5
                fenetre.blit(lifeBack, posLifeBack)
                fenetre.blit(lifeBackEnemy, posLifeBackEnemy)
                lifeBackSize = lifeBack.get_rect()
                lifeBackEnemySize = lifeBackEnemy.get_rect()
                fenetre.blit(life, (posLifeBack[0] + lifeBackSize[2] / 2 - 15, posLifeBack[1] + lifeBackSize[3] / 2))
                fenetre.blit(lifeEnemy, (posLifeBackEnemy[0] + lifeBackEnemySize[2] / 2 - 15, posLifeBackEnemy[1] + lifeBackEnemySize[3] / 2))

                # mana player and enemy
                fenetre.blit(pygame.image.load("mana.png").convert_alpha(), (screen_size[0] - 50, 40))
                fenetre.blit(pygame.image.load("mana.png").convert_alpha(), (screen_size[0] - 50,screen_size[1] - 60))
                if(playerTwo.mana > 0):
                    fenetre.blit(pygame.image.load(str(playerTwo.mana) + ".png").convert_alpha(), (screen_size[0] - 35,55))
                else:
                    fenetre.blit(pygame.image.load("0.png").convert_alpha(), (screen_size[0] - 35,55))
                if(playerOne.mana > 0):
                    fenetre.blit(pygame.image.load(str(playerOne.mana) + ".png").convert_alpha(), (screen_size[0] - 35,screen_size[1] - 45))
                else :
                    fenetre.blit(pygame.image.load("0.png").convert_alpha(), (screen_size[0] - 35,screen_size[1] - 45))
                pygame.display.flip()

                for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                    if event.type == QUIT: #Si un de ces événements est de type QUIT
                        continuer_menu = 0
                        continuer_game = 0
                        winner = False
                        continuer = 0      #On arrête la boucle

                    if event.type == KEYDOWN : # lorsqu'on appui sur un touche du clavier

                        if event.key == K_ESCAPE: # esc on retourne au menu du jeu
                            continuer_game = 0
                            continuer_menu = 1
                            continuer = 1

                    if event.type == MOUSEBUTTONUP:

                        eposx = event.pos[0]
                        eposy = event.pos[1]
                        if event.button == 1:
                            print("saisi_carte : " + str(saisi_carte))
                            print("saisi_attack : " + str(saisi_attack))
                        if saisi_carte == 0 :
                            if event.button == 1:
                                for i, carte in enumerate(playerOne.hand):
                                    carte_size = carte.carte["carte"].get_rect()
                                    posx, posy = carte.carte["posx"], carte.carte["posy"]
                                    if ( ( eposx >= posx and eposx <= (carte_size[2] + posx) ) and ( eposy >= posy and eposy <= (carte_size[3] + posy) ) ):
                                        saisi_carte = 1
                                        carte_selection = carte
                                        carte_selection_id = i
                                
                                roundButton_size = endOfRound["button"].get_rect()
                                if ( ( eposx >= endOfRound["posx"] and eposx <= (roundButton_size[2] + endOfRound["posx"]) ) and ( eposy >= endOfRound["posy"] and eposy <= (roundButton_size[3] + endOfRound["posy"]) ) ):
                                    playerTwo.pickUp(playerTwo.deck)
                                    winner = Field.playTurn2(playerTwo, playerOne)
                                    for c in playerOne.field :
                                        c.carte["statu"] = 0
                                    saisi_attack = 0
                                    playerOne.pickUp(playerOne.deck)
                                    continuer_game = 0
                        else :
                            saisi_carte = 2
                            carte_selection_id = 0
                            if ( (eposx >= carte_hand[0] and eposx < carte_hand[2] ) and (eposy < carte_hand[1]) ):
                                if(carte.carte["cost"] <= playerOne.mana) :
                                    playerOne.deploy(playerTwo, carte)
                                    Power.attackServantMultiple(playerTwo, carte)
                                    Power.addHpMaxMultiple(playerOne, playerTwo, carte)
                                    Power.pickupCard(playerOne, carte)
                                    Power.dropCard(carte, playerTwo)
                                    if len(playerTwo.field) > 0 :
                                        for c in playerTwo.field :
                                            carte_size = c.carte["carte"].get_rect()
                                            posx, posy = c.carte["posx"], c.carte["posy"]
                                            if ( (event.button == 1) and ( eposx >= posx and eposx <= (carte_size[2] + posx) ) and ( eposy >= posy and eposy <= (carte_size[3] + posy) ) ):
                                                Power.attackServant(playerOne, playerTwo, carte)
                                                Power.addHpMax(playerOne, playerTwo, carte)
                                    print("cout mana : " + str(carte.carte["cost"]))
                            continuer_game = 0

                        if saisi_attack == 0 and saisi_carte == 0 :
                            print("saisi == 0")
                            if event.button == 1 :
                                for i, carte in enumerate(playerOne.field):
                                    carte_size = carte.carte["carte"].get_rect()
                                    posx, posy = carte.carte["posx"], carte.carte["posy"]
                                    if ( ( eposx >= posx and eposx <= (carte_size[2] + posx) ) and ( eposy >= posy and eposy <= (carte_size[3] + posy) ) ):
                                        if( carte.carte["statu"] == 0 ) :
                                            saisi_attack = 1
                                            pygame.mouse.set_cursor(*pygame.cursors.diamond)
                                            carte_attack = carte
                                            carte_attack_id = i

                        if saisi_attack != 0 :
                            if event.button == 1 :
                                lifeBackEnemySize = lifeBackEnemy.get_rect()
                                xPos = posLifeBackEnemy[0] + lifeBackEnemySize[2] / 2 - 15
                                yPos = posLifeBackEnemy[1] + lifeBackEnemySize[3] / 2
                                if ( ( eposx >= xPos and eposx <= (lifeBackEnemySize[2] + xPos) ) and ( eposy >= yPos and eposy <= (lifeBackEnemySize[3] + yPos) ) ):
                                    #attack les points de vie adverse
                                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                                    carte_attack.newFight(playerOne, playerTwo)
                                    carte_attack.carte["statu"] = 1
                                    saisi_attack = 0
                                    continuer_game = 0
                                for i, carte in enumerate(playerTwo.field):
                                    carte_size = carte.carte["carte"].get_rect()
                                    posx, posy = carte.carte["posx"], carte.carte["posy"]
                                    if ( ( eposx >= posx and eposx <= (carte_size[2] + posx) ) and ( eposy >= posy and eposy <= (carte_size[3] + posy) ) ):
                                        # attack carte adverse
                                        print("attack")
                                        carte_attack.newFight(playerOne, playerTwo, carte)
                                        pygame.mouse.set_cursor(*pygame.cursors.arrow)
                                        carte_attack.carte["statu"] = 1
                                        saisi_attack = 0

                    if saisi_carte == 1 :
                        if event.type == MOUSEMOTION :
                            eposx = event.pos[0]
                            eposy = event.pos[1]
                            carte = playerOne.hand[carte_selection_id]
                            carte.carte["posx"], carte.carte["posy"] = (event.pos[0] - (carte_size[2] / 2) ), (event.pos[1] - (carte_size[3] / 2) )
                            pygame.display.flip()

                if saisi_carte == 2:
                    saisi_carte = 0

            if(playerOne.health <= 0):
                winner = playerTwo.name
                continuer_game = 0
                continuer_menu = 1
            if(playerTwo.health <= 0):
                winner = playerOne.name
                continuer_game = 0
                continuer_menu = 1
            if(winner != None):
                print("Winner : " + str(winner))



if __name__ == '__main__':
    main()
