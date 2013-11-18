#! /usr/bin/env python
# -*- coding:Utf8 -*-

'''
Created on Nov 4, 2013

@author: Simon
'''

if __name__ == '__main__':
    
#from chess.plateau import *

### Quelques fonctions d'affichage

    def manuel():
        print("Entrez ces commandes pour controler le jeu")
        print("new : nouvelle partie, save :  sauvegarder une partie, load : charger une partie")
        print("Pour jouer, entrez la position d'une piece tapez entrer. Puis entrez la position de destination de la piece")
        print("Par exemple, 1,1,1,2 pour deplacer le pion en position (1,1) vers (1,2)")
        print("Entrez man pour réimprimer ces commandes")
        print("Tapez 'quit' pour terminer la partie")
    return



    def affiche_plateau(board):
           
        unicode_dict =  {'TB': '\u2656',
                         'CB': '\u2658',
                         'FB': '\u2657',
                         'RB': '\u2654',
                         'DB': '\u2655',
                         'PB': '\u2659',
                         'TN': '\u265C',
                         'CN': '\u265E',
                         'FN': '\u265D',
                         'RN': '\u265A',
                         'DN': '\u265B',
                         'PN': '\u265F',}
        
        liste1 = board.damier.values()
        uni_list = []
        
        #Affiche un quadrillage de 0 8*8
        for x in range(0,8):
            uni_list.append(["0"]*8)  
        
        for i in liste1:
            if i != None:
                i = str(i)
                if i[2:] in unicode_dict:
                    unic = unicode_dict[i[2:]]
                    uni_list[int(i[0])][int(i[1])] = unic
                    
            
        for row in uni_list:
            print(" ".join(row))
            
  
 
    
    ### Menu principal( jeu par cr�ation, jeu par chargement)
    
    from chess.gamemanagement import GameManagement 
    debut = str(input("Bonjour! Voulez-vous creer une nouvelle partie 'new' ou charger une partie existante 'load'? "))
    play = True
    active_player = "Noir"
    while play:
        if debut.lower() == "new":
            board = GameManagement.new_game()
            
            user_input = input("C'est au tour des "+ GameManagement.alternance(active_player) +" a jouer.")
            if user_input.lower == "man":
                manuel()
            elif user_input.lower == "save":
                file_path = str(input(" "))
                GameManagement.save_game(file_path)  
            elif user_input.lower =='quit':
                play = False
            else:
                GameManagement.next_turn(user_input, board)
                active_player = GameManagement(active_player)

     
        elif debut.upper() == "load":
            save_name = input("Entrez le nom du fichier de sauvegarde sans l'extension")
            board = GameManagement.load_game(save_name)
            GameManagement.next_turn()
            
        else:
            print("Desole cette commande est inconnue")
            manuel()


    ### Menu ( jouer le tour, arr�ter et sauvegarder)
    
         
    