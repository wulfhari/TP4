'''
Created on Nov 4, 2013

@author: Simon
'''

class GameManagement():
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


    def save_game(self):
        from chess.plateau import Plateau
                     
        f = open("output.txt", "w")
        
        for item in Plateau:
            f.write(str(item) + "\n")
        
        f.close()
        
    def load_game(self):
        pass
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
    
    