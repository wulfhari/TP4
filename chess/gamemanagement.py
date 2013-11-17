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
        from chess.plateau import Plateau
### Alternance des joueurs

### Echec, echec et mat, pat, ROC

### Transformation du pion

### Interaction User/plateau


### Affichage (plateau, tour de jeu)


    def save_game(self, board):
        from os import path
        f = open("save.txt", "w")
        for item in board:
            f.write(str(item) + "\n")
        f.close()

    def load_game(self, save_file):
        from chess.plateau import Plateau
        f = open(save_file, "r")
        board = Plateau()
        for ln in f:
            line = f.readline(ln)
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
    
    def next_turn(self):
        pass
        
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
    
        
    
    