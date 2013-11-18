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
### Alternance des joueurs

### Echec, echec et mat, pat, ROC

### Transformation du pion

### Interaction User/plateau


### Affichage (plateau, tour de jeu)


    def save_game(self, board, file_name):
        import os
        cwd = os.getcwd()
        path = os.path.join(cwd, file_name)        
        f = open(path, "w")
        
        for key in board:
            if board[key][2] == T:
                
        
        for key in board.damier:
            if board.damier[(key)] != None:
                f.write(board.damier[(key)]+"\n")

            
        f.write(str(board.tour,+tour.abouge, +tour.abouge, +tour.abouge )+"\n")

        f.close()

    def load_game(self, save_file):
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
        
    
        
    def alternance(self, active_player):
        active_player = active_player
        if active_player == "Noir":
            active_player = "Blanc"
        elif active_player == "Blanc":
            active_player = "Noir"
        return active_player
    
    def next_turn(self, board):
        board.tour += 1
        
        
        
        
    def transformation(self):
        pass
    
    def echec(self):
        pass
    
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
    
        
    
    