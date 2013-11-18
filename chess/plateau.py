#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""
@file: Plateau.py
@author:  C. Besse

Fichier contenant la classe Tour
"""

from chess.tour import Tour
from chess.dame import Dame
from chess.roi import Roi
from chess.pion import Pion
from chess.fou import Fou
from chess.cavalier import Cavalier

class Plateau(object):
    tour = 0
    def __init__(self):
        """Initialise le plateau avec un damier vide"""
    #self.damier = {(0,0):Tour(0,0,0), (0,7):Tour(0,7,0), (7,0):Tour(7,0,1), (7,7):Tour(7,7,1)}
        
        self.damier = {(0,0):Tour(0,0,0), (0,1):Cavalier(0,1,0), (0,2):Fou(0,2,0), (0,3):Dame(0,3,0),(0,4):Roi(0,4,0), (0,5):Fou(0,5,0), (0,6):Cavalier(0,6,0), (0,7):Tour(0,7,0),
                       (1,0):Pion(1,0,0), (1,1):Pion(1,1,0), (1,2):Pion(1,2,0), (1,3):Pion(1,3,0),(1,4):Pion(1,4,0), (1,5):Pion(1,5,0), (1,6):Pion(1,6,0), (1,7):Pion(1,7,0),
                       (2,0):None, (2,1):None, (2,2):None, (2,3):None,(2,4):None, (2,5):None, (2,6):None, (2,7):None,
                       (3,0):None, (3,1):None, (3,2):None, (3,3):None,(3,4):None, (3,5):None, (3,6):None, (3,7):None,
                       (4,0):None, (4,1):None, (4,2):None, (4,3):None,(4,4):None, (4,5):None, (4,6):None, (4,7):None,
                       (5,0):None, (5,1):None, (5,2):None, (5,3):None,(5,4):None, (5,5):None, (5,6):None, (5,7):None,
                       (6,0):Pion(6,0,1), (6,1):Pion(6,1,1), (6,2):Pion(6,2,1), (6,3):Pion(6,3,1),(6,4):Pion(6,4,1), (6,5):Pion(6,5,1), (6,6):Pion(6,6,1), (6,7):Pion(6,7,1),
                       (7,0):Tour(7,0,1), (7,1):Cavalier(7,1,1), (7,2):Fou(7,2,1), (7,3):Dame(7,3,1),(7,4):Roi(7,4,1), (7,5):Fou(7,5,1), (7,6):Cavalier(7,6,1), (7,7):Tour(7,7,1)}
        
    def getPiece(self,line,col):
        """ReTourne la piece à la position (line,col) ou None sinon"""
        return self.damier.get((line,col))
    
    
#  Identique a :        
#        if (line,col) in self.damier.keys() :
#            return self.damier[(line,col)]
#        else:
#            return None
