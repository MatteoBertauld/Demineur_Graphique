from random import *
import pygame


##1. Fonctionel

def creerGrille():
    """ Cette fonction renvoie une liste de listes de dimension 10x10 """
    grille = [[i*0 for i in range(10)]for j in range(10)]
    grille_devoilee=[["?" for i in range(10)] for j in range(10)]
    return grille,grille_devoilee
##3. Fonctionnel

def placerMines(grille,nb_mines):
    """Cette fonction renvoie une grille contenant nb_mines mines (symbolisées par des 1)"""
    indice1 = 0
    indice2 = 0
    for i in range(nb_mines):
        indice1=randint(1,10)
        indice2=randint(1,10)
        while grille[indice1-1][indice2-1]=="X":        #Pour ne pas replacer une mine sur une autre
            indice1=randint(1,10)
            indice2=randint(1,10)
        grille[indice1-1][indice2-1]="X"
    return grille


##4. Fonctionel

def testMine(grille,i,j):
    """ Cette fonction indique si la case i,j (ligne i, colonne j) contient une mine ou pas """
    if grille[i][j]=="X":
        return True
    else:
        return False

##5

def compteMinesVoisines(grille,i,j):
    '''Cette fonction renvoie le nombre de mine présente autour d'une case'''
    nbMine=0


    if i >  0:  # != ligne haut

        if testMine(grille,i-1,j) == True:   # test mine en haut
            nbMine=nbMine+1


        if j > 0:  # != ligne gauche

            if testMine(grille,i-1,j-1) == True:  # test mine en haut à gauche
                nbMine=nbMine+1

        if j < 9:  # != ligne droite

            if testMine(grille,i-1,j+1) == True:  # test mine en haut à droite
                nbMine=nbMine+1

    if i < 9 :  # != ligne bas

        if testMine(grille,i+1,j) == True:  # test mine en bas
            nbMine=nbMine+1


        if j <9:  # != ligne droite

            if testMine(grille,i+1,j+1) == True:   # test mine en bas à droite
                nbMine=nbMine+1

        if j > 0 : # != ligne gauche

            if testMine(grille,i+1,j-1) == True:  # test mine en bas à gauche
                nbMine=nbMine+1



    if j > 0:  # != ligne gauche

        if testMine(grille,i,j-1) == True:   # test mine à gauche
            nbMine=nbMine+1




    if j < 9: # != ligne droite

        if testMine(grille,i,j+1) == True:   # test mine à droite
            nbMine=nbMine+1



    return nbMine


##6.

def demande_coordonees(grille_devoilee):
    """Cette fonction demande au joueur en quelle case il veut jouer et renvoie 1 indice pour la ligne et 1 pour la colonne"""
    colonne = int(input(bcolors.BLEU+"En quelle colonne voulez-vous jouer ? "+bcolors.RESET))
    ligne = int(input(bcolors.BLEU+"En quelle ligne voulez-vous jouer ? "+bcolors.RESET))
    if grille_devoilee[ligne-1][colonne-1]!= "?":
        text="Cette case a déja été dévoilée !"
        print (text)
    return ligne-1,colonne-1


##8

def decouvreCase(grille,grille_devoilee,i,j):
    '''met a jour la liste de listes grille_devoilee lorsque le joueur a joue le coup d'indice i,j et si le resultat est un 0, revele tout les 0 et les cases autour'''

    if grille_devoilee[i][j]== "?":

        #Revele la case
        if testMine(grille,i,j) == False:

            grille_devoilee[i][j] = compteMinesVoisines(grille,i,j)

            #Revele les cases à la suite
            if grille_devoilee[i][j]==0:
                if i>0:
                    decouvreCase(grille,grille_devoilee,i-1,j)
                    if j>0:
                        decouvreCase(grille,grille_devoilee,i-1,j-1)
                    if j<9:
                        decouvreCase(grille,grille_devoilee,i-1,j+1)
                if i<9:
                    decouvreCase(grille,grille_devoilee,i+1,j)
                    if j>0:
                        decouvreCase(grille,grille_devoilee,i+1,j-1)
                    if j<9:
                        decouvreCase(grille,grille_devoilee,i+1,j+1)
                if j<9:
                    decouvreCase(grille,grille_devoilee, i, j+1)
                if j>0:
                    decouvreCase(grille,grille_devoilee, i, j-1)
        else:

            grille_devoilee[i][j] = "X"

    return

##9.

def testVictoire(grille,grille_devoilee):
    """Test si il n'y a plus que des mines"""
    for i in range(10):
        for j in range(10):
            if grille_devoilee[i][j]=="?":
                if grille[i][j]!="X":
                    return False
    return True

##ex 7
def AfficheJeu(grille):
    """Affiche bien la grille"""
    text = ""
    print ("|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|"  )
    for i in range(10):
        for j in range(10):
            text = text +  " " + str(grille[i][j])+ " "
        if i <10:
            text = text +" | "+ str(i+1)+'\n'
    print(text)



def test():
    """Test les fonctions avec 50mines"""
    grille,grille_devoilee=creerGrille()
    grille=placerMines(grille,50)

    i,j=demande_coordonees(grille_devoilee)
    decouvreCase(grille,grille_devoilee,i,j)
    test=testMine(grille,i,j)

    nb=compteMinesVoisines(grille,i,j)
    AfficheJeu(grille)
    AfficheJeu(grille_devoilee)
    return nb,test

class bcolors: #Pour ecrire en couleur pris sur internet
    VERT = '\033[32m'
    JAUNE = '\033[33m'
    ROUGE = '\033[31m'
    BLEU = '\033[34m'
    RESET = '\033[0m'



def partie():
    """Cette fonction initie la partie"""
    grille,grille_devoilee=creerGrille()                #Crée les 2 grilles
    nbbombes=int(input(bcolors.JAUNE+"Combien de bombes voulez-vous ? "+bcolors.RESET))
    while nbbombes==0:
        print ("Il vaut mieux jouer au démineur avec des bombes ;)")
        nbbombes=int(input(bcolors.JAUNE+"Combien de bombes voulez-vous ? "+bcolors.RESET))
    grille=placerMines(grille,nbbombes)                 #Place un nombre de mine définie par le joueur
    AfficheJeu(grille_devoilee)
    # AfficheJeu(grille) Utiliser uniquement pour les tests
    while testVictoire(grille,grille_devoilee)==False:  #Tant qu'on n'a pas gagné :
        i,j=demande_coordonees(grille_devoilee)
        decouvreCase(grille,grille_devoilee,i,j)        #Revele la case choisie par le joueur
        # AfficheJeu(grille)                            #Utiliser uniquement pour les tests
        AfficheJeu(grille_devoilee)                     #Montre la grille mise à jour
        if testMine(grille,i,j)==True:                  #S'il tombe sur une mine : perdu !
            print(bcolors.ROUGE + "Vous avez perdu !" +bcolors.RESET)
            AfficheJeu(grille)
            return
    print (bcolors.VERT + "Bravo ! Vous avez gagné ! " + bcolors.RESET)  #Si toutes les cases sont dévoilés sauf les mines :
    AfficheJeu(grille)
    return


