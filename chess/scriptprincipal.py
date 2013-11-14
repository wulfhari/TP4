#! /usr/bin/env python
# -*- coding:Utf8 -*-

'''
Created on Nov 4, 2013

@author: Simon
'''

if __name__ == '__main__':
    pass

    ### Menu principal( jeu par création, jeu par chargement)
    debut = str(input("Bonjour! Voulez-vous créer une nouvelle partie (NV) ou charger une partie existante (CP)? "))
    start = True

    while start:
        if debut.upper() == "NV":
            new_game(self)
            start = False
        elif debut.upper() == "CP":
            load_game(self)
            start = False
        else:
            print ("Désolé cette entrée est inconnue, veuillez inscrire NV pour une nouvelle partie ou CP pour charger un partie existante")
        debut = str(input("Bonjour! Voulez-vous créer une nouvelle partie (NV) ou charger une partie existante (CP)? "))


    ### Menu ( jouer le tour, arrêter et sauvegarder)
    partie = str(input("Que voulez-vous faire? Jouer le tour (J), arrêter partie et sauvegarder la partie (A) ou simplement sauvegarder la partie (S)? "))
    cont = True
    while start:
        if partie.upper() == "J":
            alternance(self)
            next_turn(self)
            cont = False
        elif partie.upper() == "A":
            quitter = str(input("Êtes-vous certain de vouloir quitter? (O/N) "))
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
            print ("Désolé cette entrée est inconnue, veuillez inscrire J pour jouer le prochain tour, A pour arrêter et sauvegarder la partie ou S pour sauvegarder la partie.")

        partie = str(input("Que voulez-vous faire? Jouer le tour (J), arrêter partie et sauvegarder la partie (A) ou simplement sauvegarder la partie (S)? "))

    ### affichage ‡ chaque tour


    board = []
    for x in range(0, 7):
        board.append(["O"] * 8)

    def print_board(board):
        for row in board:
            print " ".join(row)

    print_board(board)
