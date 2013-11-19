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
    def alternance(self, board):
        
        if board.tour//2 == 0:
            active_player = 'Blanc'
        else:
            active_player = 'Noir'
        return active_player        
        '''        
        if active_player == "Noir":
            active_player = "Blanc"
        elif active_player == "Blanc":
            active_player = "Noir"
        return active_player
        '''
    
    def next_turn(self, user_input, board):
        
        
        #if GameManagement.echecEtMat != True:
        
        board.damier[(int(user_input[0]),int(user_input[1]))].deplacer((int(user_input[2]),int(user_input[3])), board)
        
        print(board.damier)
           
        
### Coups Speciaux, Echec, echec et mat, pat, ROC        
        
    def transformation(self):
        pass
    
    def echec(self, board, active_player):
        pass
        '''
        from plateau import Plateau
        from chess.plateau import Plateau
        from chess.tour import Tour
        from chess.dame import Dame
        from chess.roi import Roi
        from chess.pion import Pion
        from chess.fou import Fou
        from chess.cavalier import Cavalier
        
        f = board.damier.values()
        lsp = []
        pk = []
        
        if active_player == "Noir":
            n = 'N'
            m = 'B'
        elif active_player == "Blanc":
            n = B
            m = N
        
        for i in f:
            if i[2] == "R"+n:
                posR = (i[0],i[1])
            else:
                pass
        
        for j in f:
            if j[2] == "C"+m:
                lsp.append = (j[0],j[1])
            elif j[2] == "R"+m:
                lsp.append = (j[0],j[1])
        
        for k in f:
            if k[2] == "P"+m:
                pk.append = (k[0],k[1])
            elif k[2] == "T"+m:
                pk.append = (k[0],k[1])
            elif k[2] == "R"+m:
                pk.append = (k[0],k[1])
            elif k[2] == "F"+m:
                pk.append = (k[0],k[1])
        
        for l in lsp:
            if posR in posFuturesPossibles(lsp[l],plateau):
                return True
        for h in pk:
            if deplacementValide(pk[h],posR,plateau) == True:
                return True
        else:
            return False
            '''
    
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
    
        
    
    