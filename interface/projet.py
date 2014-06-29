import pygame
from pygame.locals import *

# initialisation de tous les modules pygame
pygame.init()

screen_size = 1300, 800
#utilisation du module display pour créé une fenetre
fenetre = pygame.display.set_mode(screen_size)


fond = pygame.image.load("Terrain.png").convert_alpha()
fond2 = pygame.image.load("terrain2.png").convert_alpha()
menu_fond = pygame.image.load("background.jpg").convert()
fenetre.blit(menu_fond, (0,0))

pos_terrain = 100, 100
size_terrain = 100, 100

carte_posx = 0
cartes = (
		 {"carte" : pygame.image.load("juda_carte.png").convert_alpha(), "name" : "juda", "posx" : 0, "posy" : 0}, 
		 {"carte" : pygame.image.load("juda_carte_pose.png").convert_alpha(), "name" : "juda_pose", "posx" : 0, "posy" : 0}, 
		 {"carte" : pygame.image.load("carte2.png").convert_alpha(), "posx" : 0, "posy" : 0}, 
		 {"carte" : pygame.image.load("carte2.png").convert_alpha(), "posx" : 0, "posy" : 0}, 
		 {"carte" : pygame.image.load("carte2.png").convert_alpha(), "posx" : 0, "posy" : 0}, 
		 {"carte" : pygame.image.load("carte2.png").convert_alpha(), "name" : "yop2", "posx" : 0, "posy" : 0}
		 )
cartes2 = (
		 {"carte" : pygame.image.load("juda_carte.png").convert_alpha(), "name" : "juda", "posx" : 0, "posy" : 0}, 
		 {"carte" : pygame.image.load("juda_carte_pose.png").convert_alpha(), "name" : "juda_pose", "posx" : 0, "posy" : 0}, 
		 {"carte" : pygame.image.load("carte2.png").convert_alpha(), "posx" : 0, "posy" : 0}, 
		 {"carte" : pygame.image.load("carte2.png").convert_alpha(), "posx" : 0, "posy" : 0}, 
		 {"carte" : pygame.image.load("carte2.png").convert_alpha(), "posx" : 0, "posy" : 0}, 
		 {"carte" : pygame.image.load("carte2.png").convert_alpha(), "name" : "yop2", "posx" : 0, "posy" : 0}
		 )
for i, carte in enumerate(cartes):
	carte_size = carte["carte"].get_rect()
	carte["posx"] = carte_posx
	carte_posx += (carte_size[2] / 4) + carte_size[2]
	carte["posy"] = screen_size[1] - (carte_size[3] + 20)

#for i, carte in enumerate(cartes2):
#	carte_size = carte["carte"].get_rect()
#	carte["posx"] = (screen_size[0] / 2) - (carte_size[2] / 2)
#	carte["posy"] = (screen_size[1] / 2) - (carte_size[3] / 2)
#	fenetre.blit(carte["carte"], (carte["posx"], carte["posy"]))
eposy = 100
menus = {"element" : pygame.image.load("bouton_1_vsIA.png").convert_alpha(), "name" : "jouer VS IA", "posx" : 0, "posy" : 0 }, {"element" : pygame.image.load("pvp.png").convert_alpha(), "name" : "jouer VS joueur", "posx" : 0, "posy" : 0 }, {"element" : pygame.image.load("bouton_quitter.png").convert_alpha(), "name" : "quitter", "posx" : 0, "posy" : 0 }
for menu in menus :
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
carte_selection_id = 0
carte_selection = ()
carte_selection_fix = ()
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
							if menu["name"] == "jouer VS joueur" :
								mode_game = 2
								continuer_menu = 0
								continuer_game = 1
								continuer = 1
								#fenetre = pygame.display.set_mode(screen_size, FULLSCREEN)

							if menu["name"] == "jouer VS IA" :
								mode_game = 1
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
		pygame.display.flip()
				
		for carte in cartes:
			fenetre.blit(carte["carte"], (carte["posx"], carte["posy"]))

		for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
			
			eposx = event.pos[0]
			eposy = event.pos[1]
			
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
				if saisi_carte == 0 :
					if event.button == 1:
						for i, carte in enumerate(cartes):
							carte_size = carte["carte"].get_rect()
							posx, posy = carte["posx"], carte["posy"]
							if ( ( eposx >= posx and eposx <= (carte_size[2] + posx) ) and ( eposy >= posy and eposy <= (carte_size[3] + posy) ) ):
								saisi_carte = 1
								carte_selection = carte["posx"], carte["posy"]
								carte_selection_id = i
				else :
					saisi_carte = 0
					carte_selection_id = 0
					if ( (eposx >= pos_terrain[0] and eposx <= ( size_terrain[0] + pos_terrain[0] )) and (eposy >= pos_terrain[1] and eposy <= (size_terrain[1] + pos_terrain[1] ) ) ):
						positionOk = 1
					else :
						positionOk = 0

			if saisi_carte != 0 :
				if event.type == MOUSEMOTION :
					eposx = event.pos[0]
					eposy = event.pos[1]
					carte = cartes[carte_selection_id]
					carte["posx"], carte["posy"] = (event.pos[0] - (carte_size[2] / 2) ), (event.pos[1] - (carte_size[3] / 2) )
					for i, c in enumerate(cartes) :
						if i == carte_selection_id :
							if positionOk == 1 :
								c = carte
#							else :
#								c["posx"], c["posy"] = carte_selection_fix[0], carte_selection_fix[1]
						fenetre.blit(c["carte"], (c["posx"], c["posy"]))
					pygame.display.flip()


# TEST ROLL OVER CARTES


			#if event.type == MOUSEMOTION :
#			for i, carte in enumerate(cartes) :
#				carte_size = carte["carte"].get_rect()
#				for j, carte2 in enumerate(cartes2) :
#					if i == j :
#						if ( ( eposx >= posx and eposx <= (carte_size[2] + posx) ) and ( eposy >= posy and eposy <= (carte_size[3] + posy) ) ):
#							carte2_size = carte2["carte"].get_rect()
#							centerx = (screen_size[0] / 2) - (carte2_size[2] / 2)
#							centery = (screen_size[1] / 2) - (carte2_size[3] / 2)
#							fenetre.blit(carte2["carte"],  (centerx, centery))
#						pygame.display.flip()




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

			
#			if event.type == MOUSEMOTION: 
#				eposx = event.pos[0]
#				eposy = event.pos[1]
#				for i, carte in enumerate(cartes) :
#					carte_size = carte["carte"].get_rect()
#					for j, carte2 in enumerate(cartes2) :
#						if i == j :
#							if ( ( eposx >= posx and eposx <= (carte_size[2] + posx) ) and ( eposy >= posy and eposy <= (carte_size[3] + posy) ) ):
#								fenetre.blit(carte2["carte"],  (carte2["posx"], carte2["posy"]))
#							pygame.display.flip()