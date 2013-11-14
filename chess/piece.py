'''
Created on Nov 5, 2013

@author: Simon
'''
from chess.tour import Tour

class piece(object):
    '''
    classdocs
    '''


    def __init__(self,line,col,couleur):
        '''
        Constructor
        '''
        """Initialise un cavalier à la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        self.line = line
        self.col = col
        self.couleur = couleur
        self.pos = [self.line, self.col]