'''
Created on Nov 5, 2013

@author: Simon
'''
class Piece(object):
    '''
    classdocs
    '''

    abouge = 1
    def __init__(self, line , col, couleur):
        '''
        Constructor
        '''
        """Initialise une piece a  la position 'ligne,colonne' avec la bonne couleur 0 pour noir, 1 pour blanc"""
        self.pos = (line,col) # Sa position
        self.color = couleur # Sa couleur ... il faudra mettre super() si on a une classe Piece mere.
        