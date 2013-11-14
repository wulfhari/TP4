#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""
@file: Plateau.py
@author:  C. Besse

Fichier contenant la classe Tour
"""

from tour import Tour

class Plateau:
    
    def __init__(self):
        """Initialise le plateau avec un damier vide"""
        self.damier = {(0,0):Tour(0,0,0), (0,7):Tour(0,7,0), (7,0):Tour(7,0,1), (7,7):Tour(7,7,1)}
        
    def getPiece(self,line,col):
        """Retourne la piece à la position (line,col) ou None sinon"""
        return self.damier.get((line,col))
#  Identique a :        
#        if (line,col) in self.damier.keys() :
#            return self.damier[(line,col)]
#        else:
#            return None
