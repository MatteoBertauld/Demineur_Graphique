import pygame
from pygame.locals import *
from Demineur_console import *
from time import sleep




def start():
    pygame.init()
    """Cette fonction sert à lancer le démineur avec l'interface graphique"""
    #Crée la fenetre
    fenetre = pygame.display.set_mode((600,600),)
    pygame.display.set_caption("Démineur Python")

    grilleJEU = pygame.image.load("image/grille.png").convert()
    drapeau = pygame.image.load("image/drapeau.png").convert()
    case = pygame.image.load("image/case.png").convert()

    fenetre.blit(grilleJEU, (0, 0)) #Affiche le tableau

    #Place un nombre de bombes choisie par le joueur
    grille,grille_devoilee=creerGrille()
    nbbombes=int(input("Combien de bombes voulez-vous ? "))
    while nbbombes==0:
        print ("Il vaut mieux jouer au démineur avec des bombes ;)")
        nbbombes=int(input("Combien de bombes voulez-vous ? "))
    grille=placerMines(grille,nbbombes)


    # Pour actualiser la fenetre
    pygame.display.flip()


    # Boucle infinie pour que tout fonctionne
    while testVictoire(grille,grille_devoilee)==False:
        active = 1
        while active == 1:
            # Recuperer tout les inputs
            for event in pygame.event.get():


                ## TESTE LES LIGNES si click gauche (1) revele si click droit (3) drapeau si click molette (2) retirer drapeau


                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] <= 60:
                    ligne = 0
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[1] <=60:
                    ligne = 0
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[1] <=60:
                    ligne = 0

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] <= 120 and event.pos[1] >60:
                    ligne = 1
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[1] <=120 and event.pos[1] > 60:
                    ligne = 1
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[1] <=120 and event.pos[1] > 60:
                    ligne = 1

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] <= 180 and event.pos[1] > 120:
                    ligne = 2
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[1] <=180 and event.pos[1] > 120:
                    ligne = 2
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[1] <=180 and event.pos[1] > 120:
                    ligne = 2

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] <= 240 and event.pos[1] > 180:
                    ligne = 3
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[1] <=240 and event.pos[1] > 180:
                    ligne = 3
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[1] <=240 and event.pos[1] > 180:
                    ligne = 3

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] <= 300 and event.pos[1] > 240:
                    ligne = 4
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[1] <=300 and event.pos[1] > 240:
                    ligne = 4
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[1] <=300 and event.pos[1] > 240:
                    ligne = 4

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] <= 360 and event.pos[1] > 300:
                    ligne = 5
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[1] <= 360 and event.pos[1] > 300:
                    ligne = 5
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[1] <= 360 and event.pos[1] > 300:
                    ligne = 5

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] <= 420 and event.pos[1] > 360:
                    ligne = 6
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[1] <= 420 and event.pos[1] > 360:
                    ligne = 6
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[1] <= 420 and event.pos[1] > 360:
                    ligne = 6

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] <= 480 and event.pos[1] > 420:
                    ligne = 7
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[1] <= 480 and event.pos[1] > 420:
                    ligne = 7
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[1] <= 480 and event.pos[1] > 420:
                    ligne = 7

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] <= 540 and event.pos[1] > 480:
                    ligne = 8
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[1] <= 540 and event.pos[1] > 480:
                    ligne = 8
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[1] <= 540 and event.pos[1] > 480:
                    ligne = 8

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1] >540:
                    ligne = 9
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[1] >540:
                    ligne = 9
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[1] >540:
                    ligne = 9

                ##TESTE COLONNES si click gauche revele si click droit drapeau si click molette retirer drapeau



                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] <= 60:
                    colonne = 0
                    revelercase(grille,grille_devoilee,ligne,colonne,fenetre)
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[0] <=60:
                    colonne = 0
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(drapeau, (60*colonne, 60*ligne))
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[0] <=60:
                    colonne = 0
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(case, (60*colonne, 60*ligne))

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] <= 120 and event.pos[0] >60:
                    colonne = 1
                    revelercase(grille,grille_devoilee,ligne,colonne,fenetre)
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[0] <=120 and event.pos[0] > 60:
                    colonne = 1
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(drapeau, (60*colonne, 60*ligne))
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[0] <=120 and event.pos[0] > 60:
                    colonne = 1
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(case, (60*colonne, 60*ligne))

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] <= 180 and event.pos[0] > 120:
                    colonne = 2
                    revelercase(grille,grille_devoilee,ligne,colonne,fenetre)
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[0] <=180 and event.pos[0] > 120:
                    colonne = 2
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(drapeau, (60*colonne, 60*ligne))
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[0] <=180 and event.pos[0] > 120:
                    colonne = 2
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(case, (60*colonne, 60*ligne))

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] <= 240 and event.pos[0] > 180:
                    colonne = 3
                    revelercase(grille,grille_devoilee,ligne,colonne,fenetre)
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[0] <=240 and event.pos[0] > 180:
                    colonne = 3
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(drapeau, (60*colonne, 60*ligne))
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[0] <=240 and event.pos[0] > 180:
                    colonne = 3
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(case, (60*colonne, 60*ligne))

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] <= 300 and event.pos[0] > 240:
                    colonne = 4
                    revelercase(grille,grille_devoilee,ligne,colonne,fenetre)
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[0] <=300 and event.pos[0] > 240:
                    colonne = 4
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(drapeau, (60*colonne, 60*ligne))
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[0] <=300 and event.pos[0] > 240:
                    colonne = 4
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(case, (60*colonne, 60*ligne))

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] <= 360 and event.pos[0] > 300:
                    colonne = 5
                    revelercase(grille,grille_devoilee,ligne,colonne,fenetre)
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[0] <= 360 and event.pos[0] > 300:
                    colonne = 5
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(drapeau, (60*colonne, 60*ligne))
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[0] <= 360 and event.pos[0] > 300:
                    colonne = 5
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(case, (60*colonne, 60*ligne))

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] <= 420 and event.pos[0] > 360:
                    colonne = 6
                    revelercase(grille,grille_devoilee,ligne,colonne,fenetre)
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[0] <= 420 and event.pos[0] > 360:
                    colonne = 6
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(drapeau, (60*colonne, 60*ligne))
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[0] <= 420 and event.pos[0] > 360:
                    colonne = 6
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(case, (60*colonne, 60*ligne))

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] <= 480 and event.pos[0] > 420:
                    colonne = 7
                    revelercase(grille,grille_devoilee,ligne,colonne,fenetre)
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[0] <= 480 and event.pos[0] > 420:
                    colonne = 7
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(drapeau, (60*colonne, 60*ligne))
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[0] <= 480 and event.pos[0] > 420:
                    colonne = 7
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(case, (60*colonne, 60*ligne))

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] <= 540 and event.pos[0] > 480:
                    colonne = 8
                    revelercase(grille,grille_devoilee,ligne,colonne,fenetre)
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[0] <= 540 and event.pos[0] > 480:
                    colonne = 8
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(drapeau, (60*colonne, 60*ligne))
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[0] <= 540 and event.pos[0] > 480:
                    colonne = 8
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(case, (60*colonne, 60*ligne))

                if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] >540:
                    colonne = 9
                    revelercase(grille,grille_devoilee,ligne,colonne,fenetre)
                if event.type == MOUSEBUTTONUP and event.button == 3 and event.pos[0] >540:
                    colonne = 9
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(drapeau, (60*colonne, 60*ligne))
                if event.type == MOUSEBUTTONUP and event.button == 2 and event.pos[0] >540:
                    colonne = 9
                    if grille_devoilee[ligne][colonne]== "?":
                        fenetre.blit(case, (60*colonne, 60*ligne))

                pygame.display.flip()



                #En cas de défaite
                if event.type == MOUSEBUTTONUP and event.button ==1:
                    if testMine(grille, ligne, colonne)==True:
                        sleep(1)
                        defaite = pygame.image.load("image/defeat.png").convert()
                        fenetre.blit(defaite ,(0,0))
                        pygame.display.flip()
                        sleep(3)
                        pygame.quit()



                #En cas de victoire
                if testVictoire(grille, grille_devoilee)==True:
                    sleep(0.5)
                    victoire = pygame.image.load("image/victory.png").convert()
                    fenetre.blit(victoire, (0,0))
                    pygame.display.flip()
                    sleep(3)
                    pygame.quit()


            #Pour fermer la fenetre
            if event.type == QUIT:
                active = 0
                pygame.quit()


def revelercase(grille,grille_devoilee,ligne,colonne,fenetre):
    """Cette fonction sert à réveller la case selectionné"""

    #Selectionne les images
    bombe = pygame.image.load("image/bombe.png").convert()
    bombe0 = pygame.image.load("image/bombe0.png").convert()
    bombe1 = pygame.image.load("image/bombe1.png").convert()
    bombe2 = pygame.image.load("image/bombe2.png").convert()
    bombe3 = pygame.image.load("image/bombe3.png").convert()
    bombe4 = pygame.image.load("image/bombe4.png").convert()
    bombe5 = pygame.image.load("image/bombe5.png").convert()
    bombe6 = pygame.image.load("image/bombe6.png").convert()
    bombe7 = pygame.image.load("image/bombe7.png").convert()
    bombe8 = pygame.image.load("image/bombe8.png").convert()


    #Affiche l'image correspondante à la case choisie
    decouvreCase(grille, grille_devoilee, ligne, colonne,fenetre)
    if grille_devoilee[ligne][colonne]==0:
        fenetre.blit(bombe0, (60*colonne, 60*ligne))

    elif grille_devoilee[ligne][colonne]==1:
        fenetre.blit(bombe1, (60*colonne, 60*ligne))

    elif grille_devoilee[ligne][colonne]==2:
        fenetre.blit(bombe2, (60*colonne, 60*ligne))

    elif grille_devoilee[ligne][colonne]==3:
        fenetre.blit(bombe3, (60*colonne, 60*ligne))

    elif grille_devoilee[ligne][colonne]==4:
        fenetre.blit(bombe4, (60*colonne, 60*ligne))

    elif grille_devoilee[ligne][colonne]==5:
        fenetre.blit(bombe5, (60*colonne, 60*ligne))

    elif grille_devoilee[ligne][colonne]==6:
        fenetre.blit(bombe6, (60*colonne, 60*ligne))

    elif grille_devoilee[ligne][colonne]==7:
        fenetre.blit(bombe7, (60*colonne, 60*ligne))

    elif grille_devoilee[ligne][colonne]==8:
        fenetre.blit(bombe8, (60*colonne, 60*ligne))

    elif grille_devoilee[ligne][colonne]=="X":
        fenetre.blit(bombe, (60*colonne, 60*ligne))
    pygame.display.flip()
    return

def decouvreCase(grille,grille_devoilee,i,j,fenetre):
    '''met a jour la liste de listes grille_devoilee lorsque le joueur a joue le coup d'indice i,j et si le resultat est un 0, revele tout les 0 et les cases autours'''

    if grille_devoilee[i][j]== "?":

        #Revele la case
        if testMine(grille,i,j) == False:

            #Selectionne les images
            bombe = pygame.image.load("image/bombe.png").convert()
            bombe0 = pygame.image.load("image/bombe0.png").convert()
            bombe1 = pygame.image.load("image/bombe1.png").convert()
            bombe2 = pygame.image.load("image/bombe2.png").convert()
            bombe3 = pygame.image.load("image/bombe3.png").convert()
            bombe4 = pygame.image.load("image/bombe4.png").convert()
            bombe5 = pygame.image.load("image/bombe5.png").convert()
            bombe6 = pygame.image.load("image/bombe6.png").convert()
            bombe7 = pygame.image.load("image/bombe7.png").convert()
            bombe8 = pygame.image.load("image/bombe8.png").convert()

            grille_devoilee[i][j] = compteMinesVoisines(grille,i,j)
            if grille_devoilee[i][j]==0:
                fenetre.blit(bombe0, (60*j, 60*i))

            elif grille_devoilee[i][j]==1:
                fenetre.blit(bombe1, (60*j, 60*i))

            elif grille_devoilee[i][j]==2:
                fenetre.blit(bombe2, (60*j, 60*i))

            elif grille_devoilee[i][j]==3:
                fenetre.blit(bombe3, (60*j, 60*i))

            elif grille_devoilee[i][j]==4:
                fenetre.blit(bombe4, (60*j, 60*i))

            elif grille_devoilee[i][j]==5:
                fenetre.blit(bombe5, (60*j, 60*i))

            elif grille_devoilee[i][j]==6:
                fenetre.blit(bombe6, (60*j, 60*i))

            elif grille_devoilee[i][j]==7:
                fenetre.blit(bombe7, (60*j, 60*i))

            elif grille_devoilee[i][j]==8:
                fenetre.blit(bombe8, (60*j, 60*i))

            elif grille_devoilee[i][j]=="X":
                fenetre.blit(bombe, (60*j, 60*i))
            pygame.display.flip()


            #Revele les cases à la suite
            if grille_devoilee[i][j]==0:
                if i>0:
                    decouvreCase(grille,grille_devoilee,i-1,j,fenetre)
                    if j>0:
                        decouvreCase(grille,grille_devoilee,i-1,j-1,fenetre)
                    if j<9:
                        decouvreCase(grille,grille_devoilee,i-1,j+1,fenetre)
                if i<9:
                    decouvreCase(grille,grille_devoilee,i+1,j,fenetre)
                    if j>0:
                        decouvreCase(grille,grille_devoilee,i+1,j-1,fenetre)
                    if j<9:
                        decouvreCase(grille,grille_devoilee,i+1,j+1,fenetre)
                if j<9:
                    decouvreCase(grille,grille_devoilee, i, j+1,fenetre)
                if j>0:
                    decouvreCase(grille,grille_devoilee, i, j-1,fenetre)
        else:

            grille_devoilee[i][j] = "X"

    return

