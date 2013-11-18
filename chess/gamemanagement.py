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
        from chess.tour import Tour
        from chess.dame import Dame
        from chess.roi import Roi
        from chess.pion import Pion
        from chess.fou import Fou
        from chess.cavalier import Cavalier
        
        board = Plateau()
        board.damier = {}
        
        file_name = file_name+".txt"
        import os
        cwd = os.getcwd()
        path = os.path.join(cwd, file_name)
            
        f = open(path, "r")
        lines = f.readlines()
        first_line = lines[0]
        pieces = {'T':Tour, 'C':Cavalier, 'F':Fou, 'D':Dame, 'R':Roi, 'P':Pion}
        couleur = {'B':1,'N':0}
        
        board.tour = first_line[0]
        
        for i in range(1,len(lines)):
            line = lines[i]
            board.damier[(int(line[0]),int(line[1]))] = pieces[line[2]](int(line[0]),int(line[1]),couleur[line[3]])
            
        if board.damier[(7,7)] != None:    
            board.damier[(7,7)].abouge = int(first_line[2])
        elif board.damier[(7,0)] != None:    
            board.damier[(7,0)].abouge = int(first_line[4])
        elif board.damier[(0,7)] != None:
            board.damier[(0,7)].abouge = int(first_line[6])
        elif board.damier[(0,0)] != None:
            board.damier[(0,0)].abouge = int(first_line[8])
        
        
        f.close()
       
        return board
       
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
        from plateau import Plateau
        f = board.damier.values()
    
        if active_player == "Noir":
            n = RN
        elif active_player == "Blanc":
            n = RB
        for i in f:
            if i[2:] == n:
                posR = (i[0],i[1])
            else:
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
    
        
    
    