'''
Created on Nov 16, 2013

@author: Simon
'''
from chess.piece import Piece

class Dame(Piece):
    '''
    classdocs
    '''


    def __init__(self,line,col,couleur):
        """Initialise un roi a la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        Piece.__init__(self,line,col,couleur)
        