#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on Nov 4, 2013

@author: Simon
'''

class GameManagement(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''




### Interaction User/plateau


### Affichage (plateau, tour de jeu)


    def save_game(self, board, file_name):
        file_name = file_name+".txt"
        import os
        cwd = os.getcwd()
        path = os.path.join(cwd, file_name)        
        f = open(path, "w")
        Line1_list = [board.tour, board.damier[(0,0)].abouge, board.damier[(0,7)].abouge, board.damier[(7,0)].abouge, board.damier[(7,7)].abouge]
        for i in Line1_list:
            f.write(str(i)+" ")
        f.write("\n") 
               
        for key in board.damier:
            if board.damier[(key)] != None:
                f.write(str((board.damier[(key)]))+"\n")    
        f.close()

    def load_game(self, file_name):
        from chess.plateau import Plateau
        f = open(save_file, "r")
        board = Plateau()
        board.damier = {}
        for ln in range(1,len(f)):
            line = f.readline(ln)
            line[0] = 
            board[line()] = line()
        return board
        f.close()
    
    def new_game(self):
        from chess.plateau import Plateau
        board = Plateau()
        return board
        
    
### Alternance des joueurs        
    def alternance(self, active_player):
        active_player = active_player
        if active_player == "Noir":
            active_player = "Blanc"
        elif active_player == "Blanc":
            active_player = "Noir"
        return active_player
    
    def next_turn(self, board):
        board.tour += 1
        
        
### Coups Speciaux, Echec, echec et mat, pat, ROC        
        
    def transformation(self):
        pass
    
    def echec(self):
        hello world
    
    def echecEtMat(self):
        pass
    
    def pat(self, board):
        pass
    
    def en_passant(self):
        pass
    
    def no_suicide(self): 
        pass
    
    def ROC(self):
        pass
    
        
    
    