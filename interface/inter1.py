import pygame
from pygame.locals import *


# initialisation de tous les modules pygame
pygame.init()

screen_size = 1300, 800
#utilisation du module display pour créé une fenetre
fenetre = pygame.display.set_mode(screen_size)


fond = pygame.image.load("Terrain.png").convert_alpha()
fond2 = pygame.image.load("terrain2.png").convert_alpha()
menu_fond = pygame.image.load("fondPython.jpeg").convert()
fenetre.blit(menu_fond, (0,0))

pos_terrain = 100, 100
size_terrain = 100, 100

carte_terrain = 0, 500, 1300, 800


carte_posx = 200
fields = []

cartes = [
			{"carte" : pygame.image.load("juda_carte.png").convert_alpha(), "attack" : 9, "health" : 5, "attackImg" : pygame.image.load("9.png").convert_alpha(), "healthImg" : pygame.image.load("5.png").convert_alpha(), "attackPosx" : 0, "attackPosy" : 0, "healthPosx" : 0, "healthPosy" : 0, "posx" : 0, "posy" : 0},
			{"carte" : pygame.image.load("juda_carte_pose.png").convert_alpha(), "attack" : 9, "health" : 5, "attackImg" : pygame.image.load("9.png").convert_alpha(), "healthImg" : pygame.image.load("5.png").convert_alpha(), "attackPosx" : 0, "attackPosy" : 0, "healthPosx" : 0, "healthPosy" : 0, "posx" : 0, "posy" : 0}, 
			{"carte" : pygame.image.load("carte2.png").convert_alpha(), "attack" : 9, "health" : 5, "attackImg" : pygame.image.load("9.png").convert_alpha(), "healthImg" : pygame.image.load("5.png").convert_alpha(), "attackPosx" : 0, "attackPosy" : 0, "healthPosx" : 0, "healthPosy" : 0, "posx" : 0, "posy" : 0}, 
			{"carte" : pygame.image.load("carte2.png").convert_alpha(), "attack" : 9, "health" : 5, "attackImg" : pygame.image.load("9.png").convert_alpha(), "healthImg" : pygame.image.load("5.png").convert_alpha(), "attackPosx" : 0, "attackPosy" : 0, "healthPosx" : 0, "healthPosy" : 0, "posx" : 0, "posy" : 0}, 
			{"carte" : pygame.image.load("carte2.png").convert_alpha(), "attack" : 9, "health" : 5, "attackImg" : pygame.image.load("9.png").convert_alpha(), "healthImg" : pygame.image.load("5.png").convert_alpha(), "attackPosx" : 0, "attackPosy" : 0, "healthPosx" : 0, "healthPosy" : 0, "posx" : 0, "posy" : 0}, 
			{"carte" : pygame.image.load("carte2.png").convert_alpha(), "attack" : 9, "health" : 5, "attackImg" : pygame.image.load("9.png").convert_alpha(), "healthImg" : pygame.image.load("5.png").convert_alpha(), "attackPosx" : 0, "attackPosy" : 0, "healthPosx" : 0, "healthPosy" : 0, "posx" : 0, "posy" : 0}
			#{"carte" : pygame.image.load("juda_carte.png").convert_alpha(), "posx" : 0, "posy" : 0},
			#{"carte" : pygame.image.load("juda_carte_pose.png").convert_alpha(), "posx" : 0, "posy" : 0}, 
			#{"carte" : pygame.image.load("carte2.png").convert_alpha(), "posx" : 0, "posy" : 0}, 
			#{"carte" : pygame.image.load("carte2.png").convert_alpha(), "posx" : 0, "posy" : 0}, 
			#{"carte" : pygame.image.load("carte2.png").convert_alpha(), "posx" : 0, "posy" : 0}, 
			#{"carte" : pygame.image.load("carte2.png").convert_alpha(), "posx" : 0, "posy" : 0}
		 ]


for carte in cartes:
	carte_size = carte["carte"].get_rect()
	carte["posx"] = carte_posx
	carte_posx += (carte_size[2] / 3)
	carte_posy = carte["posy"]
	carte["posy"] = screen_size[1] - (carte_size[3] + 20)
endOfRound = {"button" : pygame.image.load("endOfRound.png").convert_alpha(), "name" : "yop", "posx" : 1000, "posy" : 350}

eposy = 100
menus = [
			{"element" : pygame.image.load("bouton_1_vsIA.png").convert_alpha(), "name" : "jouer VS IA", "posx" : 10, "posy" : 100 },
			{"element" : pygame.image.load("pvp.png").convert_alpha(), "name" : "jouer VS joueur", "posx" : 900, "posy" : 100 },
			{"element" : pygame.image.load("bouton_quitter.png").convert_alpha(), "name" : "quitter", "posx" : 30, "posy" : 250 }
		]

for i, menu in enumerate(menus) :
#	menu_size = menu["element"].get_rect()
#	menu["posx"] = (screen_size[0] / 2) - (menu_size[2] / 2) 
#	menu["posy"] = eposy
	fenetre.blit(menu["element"], (menu["posx"], menu["posy"]))
#	eposy += (menu_size[3] / 2) + menu_size[3]

pygame.display.flip()

mode_game = 0
continuer = 1
continuer_menu = 1
continuer_game = 1
saisi_carte = 0
carte_selection_id = 0
carte_selection = ()
deplacement = 5
positionOk = 0
pygame.key.set_repeat(400, 30)

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
				continuer = 0

			if event.type == KEYDOWN : # lorsqu'on appui sur un touche du clavier

				if event.key == K_ESCAPE: # esc on quitte le jeu
					continuer_game = 0
					continuer_menu = 0
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
								#fenetre = pygame.display.set_mode(screen_size, FULLSCREEN)
							if menu["name"] == "jouer VS joueur" :
								mode_game = 2
								continuer_menu = 0
								continuer_game = 1
								continuer = 1
								#fenetre = pygame.display.set_mode(screen_size, FULLSCREEN)
							if menu["name"] == "quitter" :
								mode_game = 0
								continuer_menu = 0
								continuer_game = 0
								continuer = 0

				if event.button == 1 :
					print( event.pos )
				if event.button == 3 :
					print("Click Droit")
				if event.button == 4 :
					print("Molette haute")
				if event.button == 5 :
					print("Molette basse")
				if event.button == 2 :
					print("Click Molette")

	while continuer_game: # boucle du jeu


		fenetre.blit(fond, (0, 0))
		fenetre.blit(fond2, (0, 0))

		for carte in cartes:
			fenetre.blit(carte["carte"], (carte["posx"], carte["posy"]))
			carte_size = carte["carte"].get_rect()
			#print(carte_size)
			carte["attackPosx"] = carte["posx"] + (carte_size[2] / 15)
			carte["attackPosy"] = carte["posy"] + (carte_size[3] - (carte_size[3] / 9))
			carte["healthPosx"] = carte["posx"] + (carte_size[2] - (carte_size[2] / 5))
			carte["healthPosy"] = carte["posy"] + (carte_size[3] - (carte_size[3] / 9))
			fenetre.blit(carte["attackImg"], (carte["attackPosx"], carte["attackPosy"]))
			fenetre.blit(carte["healthImg"], (carte["healthPosx"], carte["healthPosy"]))

		fenetre.blit(endOfRound["button"], (endOfRound["posx"], endOfRound["posy"]))

		for carte in fields:
			fenetre.blit(carte["carte"], (carte["posx"], carte["posy"]))

		pygame.display.flip()
				

		for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
			if event.type == QUIT: #Si un de ces événements est de type QUIT
				continuer_menu = 0
				continuer_game = 0
				continuer = 0      #On arrête la boucle

			if event.type == KEYDOWN : # lorsqu'on appui sur un touche du clavier

				if event.key == K_ESCAPE: # esc on retourne au menu du jeu
					continuer_game = 0
					continuer_menu = 1
					continuer = 1

			if event.type == MOUSEBUTTONUP:
				print(cartes)
				print(fields)
				eposx = event.pos[0]
				eposy = event.pos[1]
				if saisi_carte == 0 :
					if event.button == 1:
						for i, carte in enumerate(cartes):
							carte_size = carte["carte"].get_rect()
							posx, posy = carte["posx"], carte["posy"]
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
							if( cartes != [] ):
								for carte in cartes:
									carte_size = carte["carte"].get_rect()
									x = (carte_size[2] / 3)
									carte_posx += x
									y = screen_size[1] - (carte_size[3] + 20)
							cartes.append({"carte" : pygame.image.load("carte2.png").convert_alpha(), "name" : "yop2", "posx" : (x + carte_posx), "posy" : y})
				else :
					saisi_carte = 0
					carte_selection_id = 0
#					if ( (eposx >= pos_terrain[0] and eposx <= ( size_terrain[0] + pos_terrain[0] )) and (eposy >= pos_terrain[1] and eposy <= (size_terrain[1] + pos_terrain[1] ) ) ):
					if ( (eposx >= carte_terrain[0] and eposx < carte_terrain[2] ) and (eposy < carte_terrain[1]) ):
						fields.append(carte_selection)
						cartes.remove(carte_selection)

			if saisi_carte != 0 :
				if event.type == MOUSEMOTION :
					eposx = event.pos[0]
					eposy = event.pos[1]
					carte = cartes[carte_selection_id]
					carte["posx"], carte["posy"] = (event.pos[0] - (carte_size[2] / 2) ), (event.pos[1] - (carte_size[3] / 2) )
					for i, c in enumerate(cartes) :
#						if i == carte_selection_id :
#							if positionOk == 1 :
#								c = carte
						fenetre.blit(c["carte"], (c["posx"], c["posy"]))
					for i, c in enumerate(fields) :
						fenetre.blit(c["carte"], (c["posx"], c["posy"]))
					pygame.display.flip()



			if event.type == MOUSEBUTTONUP: 
				if event.button == 1 :
					print( event.pos )
				if event.button == 3 :
					print("Click Droit")
				if event.button == 4 :
					print("Molette haute")
				if event.button == 5 :
					print("Molette basse")
				if event.button == 2 :
					print("Click Molette")
