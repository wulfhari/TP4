#! /usr/bin/env python
# -*- coding:Utf8 -*-

'''
Created on Nov 4, 2013

@author: Simon
'''

if __name__ == '__main__':
    
#from chess.plateau import *

    ### Menu principal( jeu par cr�ation, jeu par chargement)
    from chess.gamemanagement import * 
    debut = str(input("Bonjour! Voulez-vous creer une nouvelle partie new ou charger une partie existante (load)? "))
    play = True
    while play:
        if debut.lower() == "new":
            board = new_game()
            
        elif debut.upper() == "load":
            board = load_game()
            next
        else:
            print("Desole cette commande est inconnue")
            manuel()


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

    def manuel():
        print("Entrez ces commandes pour controler le jeu")
        print("new : nouvelle partie, save :  sauvegarder une partie, load : charger une partie")
        print("Pour jouer, entrez la position d'une piece tapez entrer. Puis entrez la position de destination de la piece")
        print("Par exemple, (1,1)(1,2) pour deplacer le pion en position (1,1) vers (1,2) ))
        print("Entrez man pour réimprimer ces commandes")
        
    def affichage_plateau():
        from chess.plateau import Plateau
        board = Plateau()
        
        
        caracteres_unicode_pieces = {'TB': '\u2656',
                                     'CB': '\u2658',
                                     'FB': '\u2657',
                                     'KB': '\u2654',
                                     'QB': '\u2655',
                                     'PB': '\u2659',
                                     'TN': '\u265C',
                                     'CN': '\u265E',
                                     'FN': '\u265D',
                                     'KN': '\u265A',
                                     'QN': '\u265B',
                                     'PN': '\u265F',}
  
     
    """
    for x in range(0, 7):
        board.append(["O"] * 8)

    def print_board(board):
        for row in board:
            print " ".join(row)

    print_board(board)
    """