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
from CardSet import CardSet
from Field import Field
import pygame
from pygame.locals import *

def main():

    pygame.init()
    screen_size = 1300, 800
    fenetre = pygame.display.set_mode(screen_size)

    fondEcran = ["salle", "Terrain"]
    numFond = random.randint(0, len(fondEcran) - 1)
    fond = pygame.image.load(fondEcran[numFond] + ".png").convert_alpha()
    #fond = pygame.image.load("Terrain.png").convert_alpha()
    fond2 = pygame.image.load("terrain2.png").convert_alpha()
    menu_fond = pygame.image.load("fondPython.jpeg").convert()
    fenetre.blit(menu_fond, (0,0))

    pos_terrain = 100, 100
    size_terrain = 100, 100

    carte_hand = 0, 500, 1300, 800
    carte_field = 0, 500, 1300, 800
    carte_ennemyHand = 0, 500, 1300, 800
    carte_ennemyField = 0, 500, 1300, 800


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
#                print("DEBUG : playerOne.hand" + str(c.carte))

            carte_posx = 400
            for c in playerTwo.hand :
                # positionnement des cartes ennemies dans sa main
                c.carte["carte"] = pygame.image.load("carte_dos.png").convert_alpha()
                carte_size = c.carte["carte"].get_rect()
                c.carte["posx"] = carte_posx
                carte_posx += (carte_size[2] / 3)
                c.carte["posy"] = 20
#                print("DEBUG : playerTwo.hand" + str(c.carte))

            carte_posx = 250
            for c in playerOne.field :
                c.carte["carte"] = pygame.image.load(str(c.carte["name"]) + "_pose.png").convert_alpha()
                carte_size = c.carte["carte"].get_rect()
                c.carte["posx"] = carte_posx
                carte_posx += carte_size[2] + 5
                c.carte["posy"] = (screen_size[1] / 2) - 5
#                print("DEBUG : playerOne.Field" + str(c.carte))

            carte_posx = 250
            for c in playerTwo.field :
                c.carte["carte"] = pygame.image.load(str(c.carte["name"]) + "_pose.png").convert_alpha()
                carte_size = c.carte["carte"].get_rect()
                c.carte["posx"] = carte_posx
                carte_posx += carte_size[2] + 5
                c.carte["posy"] = (screen_size[1] / 2) - 100
#                print("DEBUG : playerTwo.Field" + str(c.carte))

            lifeBack = pygame.image.load("vie.png").convert_alpha()
            lifeBackEnemy = pygame.image.load("vie.png").convert_alpha()
            life = pygame.image.load(str(playerOne.health) + "_vie.png").convert_alpha()
            lifeEnemy = pygame.image.load(str(playerTwo.health) + "_vie.png").convert_alpha()
            fenetre.blit(lifeBackEnemy, (0, 0))
            while continuer_game: # boucle du jeu


                fenetre.blit(fond, (0, 0))
                fenetre.blit(fond2, (0, 0))
                for c in playerOne.hand:
                    # positionnement des cartes dans la main
                    fenetre.blit(c.carte["carte"], (c.carte["posx"], c.carte["posy"]))
                    carte_size = c.carte["carte"].get_rect()
                    c.carte["attackImg"] = pygame.image.load(str(c.carte["attack"]) + ".png").convert_alpha()
                    c.carte["healthImg"] = pygame.image.load(str(c.carte["health"]) + ".png").convert_alpha()
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

                for c in playerOne.field:
                    # positionnement des cartes sur le térrain
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
                fenetre.blit(pygame.image.load(str(playerTwo.mana) + ".png").convert_alpha(), (screen_size[0] - 35,55))
                fenetre.blit(pygame.image.load(str(playerOne.mana) + ".png").convert_alpha(), (screen_size[0] - 35,screen_size[1] - 45))
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
                        #print(playerOne.hand)
                        #print(fields)
                        eposx = event.pos[0]
                        eposy = event.pos[1]
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
                                    x = 0
                                    carte_posx = 200
                                    c = pygame.image.load("carte2.png").convert_alpha()
                                    cSize = c.get_rect()
                                    y = screen_size[1] - (cSize[3] + 20)
                                    if( playerOne.hand != [] ):
                                        for carte in playerOne.hand:
                                            carte_size = carte.carte["carte"].get_rect()
                                            x = (carte_size[2] / 3)
                                            carte_posx += x
                                            y = screen_size[1] - (carte_size[3] + 20)
                                    playerOne.pickUp(playerOne.deck)
                                    playerTwo.pickUp(playerTwo.deck)
                                    continuer_game = 0
                        else :
                            saisi_carte = 0
                            carte_selection_id = 0
                            if ( (eposx >= carte_hand[0] and eposx < carte_hand[2] ) and (eposy < carte_hand[1]) ):
                                if(carte.carte["cost"] <= playerOne.mana) :
                                    playerOne.deploy(playerTwo, carte)
                                    print("cout mana : " + str(carte.carte["cost"]))
                            continuer_game = 0

                        if saisi_attack == 0 :
                            if event.button == 1 :
                                for i, carte in enumerate(playerOne.field):
                                    carte_size = carte.carte["carte"].get_rect()
                                    posx, posy = carte.carte["posx"], carte.carte["posy"]
                                    if ( ( eposx >= posx and eposx <= (carte_size[2] + posx) ) and ( eposy >= posy and eposy <= (carte_size[3] + posy) ) ):
                                        if saisi_carte == 0 :
                                            saisi_attack = 1
                                            pygame.mouse.set_cursor(*pygame.cursors.diamond)
                                            carte_attack = carte
                                            carte_attack_id = i

                        if saisi_attack != 0 :
                            if event.button == 1 :
                                for i, carte in enumerate(playerTwo.field):
                                    carte_size = carte.carte["carte"].get_rect()
                                    posx, posy = carte.carte["posx"], carte.carte["posy"]
                                    if ( ( eposx >= posx and eposx <= (carte_size[2] + posx) ) and ( eposy >= posy and eposy <= (carte_size[3] + posy) ) ):
                                        carte_attack.fight(carte)
                                        pygame.mouse.set_cursor(*pygame.cursors.arrow)



                    if saisi_carte != 0 :
                        if event.type == MOUSEMOTION :
                            eposx = event.pos[0]
                            eposy = event.pos[1]
                            carte = playerOne.hand[carte_selection_id]
                            carte.carte["posx"], carte.carte["posy"] = (event.pos[0] - (carte_size[2] / 2) ), (event.pos[1] - (carte_size[3] / 2) )
    #                        for i, c in enumerate(playerOne.hand) :
    #                            fenetre.blit(c.carte["carte"], (c.carte["posx"], c.carte["posy"]))
    #                        for i, c in enumerate(fields) :
    #                            fenetre.blit(c.carte["carte"], (c.carte["posx"], c.carte["posy"]))
                            pygame.display.flip()
            if(playerOne.health <= 0):
                winner = playerTwo.name
                continuer_game = 0
                continuer_menu = 1
            if(playerTwo.health <= 0):
                winner = playerOne.name
                continuer_game = 0
                continuer_menu = 1
            print("playerOne vie :" + str(playerOne.health))
            print("playerTwo vie :" + str(playerTwo.health))
            if(winner != None):
                print("Winner : " + winner)

#        print(sys.version)
#        i = 1
#        winner = None
#        while winner == None :
#            if i % 2 == 0 :
#                winner = Field.playTurn(playerOne, playerTwo)
#            else :
#                winner = Field.playTurn(playerTwo, playerOne)
#            i += 1
#        playerOne.toString()
#        playerTwo.toString()
#        print("Vainqueur : ", winner.name)




if __name__ == '__main__':
    main()