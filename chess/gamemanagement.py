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


    def save_game(self, Plateau):
        
                     
        f = open("save.txt", "w")
        for item in Plateau:
            f.write(str(item) + "\n")
        f.close()
        
    def load_game(self):
        f = open("save.txt", "r")
        for ln in f:
            line = f.readline(ln)
            Plateau.damier[] = line
        f.close()
    
    def new_game(self):
        pass
    def next_turn(self):
        pass
    def alternance(self):
        pass
    def echec(self):
        pass
    def transformation(self):
        pass
    def echecEtMat(self):
        pass
    def PAT(self):
        pass
    def ROC(self):
        pass
    
    