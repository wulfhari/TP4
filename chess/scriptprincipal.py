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
            
  
 
    
    ### Menu principal jeu par creation, jeu par chargement
    
    from chess.gamemanagement import GameManagement 
    GM = GameManagement()
    debut = str(input("Bonjour! Voulez-vous creer une nouvelle partie 'new'; charger une partie existante 'load'?; ou quitter 'quit' "))
    on = True
    active_player = "Noir"
    numbers = ['0','1','2','3','4','5','6','7']
    while on:
        if debut.lower() == "new":
            play = True
            board = GM.new_game()
            affiche_plateau(board)
            user_input = input("C'est au tour des "+ GM.alternance(board) +" a jouer.")
            
            ###  jouer le tour, arreter , sauvegarder, manuel d instruction
            
            while play:
                if user_input.lower() == "man":
                    manuel()
                elif user_input.lower() == "save":
                    file_name = str(input(" Entrez le nom du fichier de sauvegarde "))
                    GM.save_game(file_name)  
                elif user_input.lower() =='quit':
                    play = False
                    
                elif user_input.lower()[0] in numbers:
                    GM.next_turn(user_input, board)
                    if board.damier[(int(user_input[0]),int(user_input[1]))] == None:
                        board.tour += 1
                        active_player = GM.alternance(active_player)
                        affiche_plateau(board)
                        user_input = input("C'est au tour des "+ GM.alternance(active_player) +" a jouer.")
                    else:
                        print('Ce coup est invalide entrez de nouvelles coordonnees')
                        user_input = input("C'est au tour des "+ GM.alternance(active_player) +" a jouer.")
                else:
                    print("Ceci n'est pas une commande reconnue")
                    manuel()
     
        elif debut.lower() == "load":
            play = True
            save_name = str(input("Entrez le nom du fichier de sauvegarde sans l'extension"))
            board = GM.load_game(save_name)
            affiche_plateau(board)
            
                       
            user_input = input("C'est au tour des "+ GM.active_player(board) +" a jouer.")
            
            while play:
                if user_input.lower() == "man":
                    manuel()
                elif user_input.lower() == "save":
                    file_name = str(input(" Entrez le nom du fichier de sauvegarde "))
                    GM.save_game(file_name)  
                elif user_input.lower() =='quit':
                    play = False
                    
                elif user_input.lower()[0] in numbers:
                    GM.next_turn(user_input, board)
                    active_player = GameManagement.alternance(active_player)
                else:
                    print("Ceci n'est pas une commande reconnue")
                    manuel()
        elif debut == 'quit':
            print('Bebye')
            on = False
                    
        else:
            print("Desole cette commande est inconnue")
            debut = str(input("Entrez 'new' ou 'load' pour commencer une partie."))


  
    
         
    