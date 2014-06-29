import pygame
from pygame.locals import *

# initialisation de tous les modules pygame
pygame.init()

t = 640, 480

#utilisation du module display pour créé une fenetre
fenetre = pygame.display.set_mode(t, RESIZABLE)


fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))


#image.set_colorkey((255,0,0))


perso = pygame.image.load("perso.png").convert_alpha()
t_perso = perso.get_rect()
fenetre.blit(perso, t_perso)


pygame.display.flip()

continuer = 1
deplacement = 5
pygame.key.set_repeat(400, 30)

while continuer :
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:# or event.type == K_ESCAPE:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle

		if event.type == KEYDOWN :

			if event.key == K_DOWN :
				t_perso = t_perso.move(0, deplacement)
				#t_perso = (t_perso[0], (t_perso[1] + 10))
				print(t_perso)

			if event.key == K_UP :
				t_perso = t_perso.move(0, -deplacement)
				#t_perso = (t_perso[0], (t_perso[1] - 10))
				print(t_perso)

			if event.key == K_LEFT :
				t_perso = t_perso.move(-deplacement, 0)
				#t_perso = ((t_perso[0] - 10), t_perso[1])
				print(t_perso)

			if event.key == K_RIGHT :
				t_perso = t_perso.move(deplacement, 0)
				#t_perso = ((t_perso[0] + 10), t_perso[1])
				print(t_perso)

			if event.key == K_ESCAPE:
				continuer = 0

		#if event.type == MOUSEBUTTONDOWN:
			# click down
		if event.type == MOUSEMOTION and event.buttons[0] == 1 :
			fenetre.blit(fond, (0, 0))
			t_perso = event.pos[0], event.pos[1]
			fenetre.blit(perso, t_perso)
			pygame.display.flip()
			
			#carte_size = carte.get_rect()
			#fenetre.blit(fond, (0, 0))
			#if( ( posx >= carte_pos[0] and posx <= (carte_size[2] + carte_pos[0]) ) and ( posy >= carte_pos[1] and posy <= (carte_size[3] + carte_pos[1]) ) ):
			#	carte_pos = (event.pos[0] - (carte_size[2] / 2) ), (event.pos[1] - (carte_size[3] / 2) )
			#	posx, posy = event.pos[0], event.pos[1]
			#	fenetre.blit(carte, carte_pos)
			#	fenetre.blit(perso, t_perso)
			#	pygame.display.flip()

			

#			if event.type == MOUSEMOTION and event.buttons[0] == 1: # click et mouvement de souris
#				eposx = event.pos[0]
#				eposy = event.pos[1]
#				for carte in cartes:
#					carte_size = carte["carte"].get_rect()
#					posx, posy = carte["posx"], carte["posy"]
#					fenetre.blit(fond, (0, 0))
#					fenetre.blit(fond2, (0, 0))
#					if( ( eposx >= posx and eposx <= (carte_size[2] + posx) ) and ( eposy >= posy and eposy <= (carte_size[3] + posy) ) ):
#						carte["posx"], carte["posy"] = (event.pos[0] - (carte_size[2] / 2) ), (event.pos[1] - (carte_size[3] / 2) )
#						for c in cartes :²
#							fenetre.blit(c["carte"], (c["posx"], c["posy"]))
#						pygame.display.flip()


		if event.type == MOUSEBUTTONUP: 
			# click up 
			# event.button = 1  : click gauche
			# event.button = 3  : click droit
			# event.button = 2  : click molette ou droite + gauche
			# event.button = 4 || 5 : molette
			if event.button == 1 :
				print("Click Gauche")
			if event.button == 3 :
				print("Click Droit")


			
	fenetre.blit(fond, (0, 0))
	fenetre.blit(perso, t_perso)
	pygame.display.flip()
			