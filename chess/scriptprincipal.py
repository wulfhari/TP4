#! /usr/bin/env python
# -*- coding:Utf8 -*-

'''
Created on Nov 4, 2013

@author: Simon
'''

if __name__ == '__main__':
    
from chess.plateau import *

    ### Menu principal( jeu par cr�ation, jeu par chargement)
    def menu_princ():
        debut = str(input("Bonjour! Voulez-vous creer une nouvelle partie (NV) ou charger une partie existante (CP)? "))
        start = True

        while start:
            if debut.upper() == "NV":
                new_game(self)
                start = False
            elif debut.upper() == "CP":
                load_game(self)
                start = False
            else:
                print ("Desole cette entree est inconnue, veuillez inscrire NV pour une nouvelle partie ou CP pour charger un partie existante")
            debut = str(input("Bonjour! Voulez-vous creer une nouvelle partie (NV) ou charger une partie existante (CP)? "))


    ### Menu ( jouer le tour, arr�ter et sauvegarder)
    
    def menu_tour():
        partie = str(input("Que voulez-vous faire? Jouer le tour (J), arreter le partie et sauvegarder la partie (A) ou simplement sauvegarder la partie (S)? "))
        cont = True
        while start:
            if partie.upper() == "J":
                alternance(self)
                next_turn(self)
                cont = False
            elif partie.upper() == "A":
                quitter = str(input("etes-vous certain de vouloir quitter? (O/N) "))
                    if quitter.upper() == "O":
                        save_game(self)
                        quit_game(self)
                        cont = False
                    elif quitter.upper() == "N":
                        pass
                    else:
                        print ("Veuillez inscrire O pour Oui ou N pour Non")
            elif partie.upper() == "S":
                save_game(self)
                cont = False
            else:
                print ("Desole cette entree est inconnue, veuillez inscrire J pour jouer le prochain tour, A pour arr�ter et sauvegarder la partie ou S pour sauvegarder la partie.")

            partie = str(input("Que voulez-vous faire? Jouer le tour (J), arr�ter partie et sauvegarder la partie (A) ou simplement sauvegarder la partie (S)? "))

    def commandes():
        
    
    ### affichage � chaque tour


board = Plateau.damier

game = "on"
while game == "on"
    print("Bienvenu dans le jeu Completement Echec v1.0")
    print("En tout temps, vous pouvez entrer ces commandes pour controler le jeu")
    print("new : nouvelle partie, save :  sauvegarder une partie, load : charger une partie")
    print("Pour jouer, entrez la position d'une piece tapez entrer. Puis entrez la position de destination de la piece")
    print("com : réimprimer ces commandes")
    
   
    """
    for x in range(0, 7):
        board.append(["O"] * 8)

    def print_board(board):
        for row in board:
            print " ".join(row)

    print_board(board)
    """