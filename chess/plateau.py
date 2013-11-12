#! c:/Python33 python
# -*- coding:Utf-8 -*-

"""
@file: plateau.py
@author:  C. Besse

Fichier contenant la classe Tour
"""

"""

from chess.tour import Tour

class Plateau:
    
    def __init__(self):
        """Initialise le plateau avec un damier vide"""
        self.damier = {(0,0):Tour(0,0,0), (0,7):Tour(0,7,0), (7,0):Tour(7,0,1), (7,7):Tour(7,7,1)}
        
    def getPiece(self,line,col):
        """Retourne la piece à la position (line,col) ou None sinon"""
        pass
"""

#! /usr/bin/env python
# -*- coding:Utf8 -*-

"""
@file: Tp4_CL.py
@author:  C. Laurendeau

"""
from echecClasses import *
 
#Les variables.
j = Joueur()
p = Piece()
 
#Le programme principal
j.selectPiece()
j.updatePlateau()
print(p.get_plateau()) #On veut voir le résultat


#Classe Plateau

class Plateau (object):
    """
    Initialisation du plateau de jeu, du temps, du score, qui doit jouer
    """
    def __init__(self):
        
        self.plateau = {
                       "0,0":"tourG-b", "0,1":"cavalierG-b", "0,2":"fouG-b", "0,3":"dame-b",
                       "0,4":"roi-b", "0,5":"fouD-b", "0,6":"cavalierD-b", "0,7":"tourD-b",
  
                       "1,0":"pion-b", "1,1":"pion-b", "1,2":"pion-b", "1,3":"pion-b",
                       "1,4":"pion-b", "1,5":"pion-b", "1,6":"pion-b", "1,7":"pion-b",
  
                       "2,0":None, "2,1":None, "2,2":None, "2,3":None,
                       "2,4":None, "2,5":None, "2,6":None, "2,7":None,
  
                       "3,0":None, "3,1":None, "3,2":None, "3,3":None,
                       "3,4":None, "3,5":None, "3,6":None, "3,7":None,
  
                       "4,0":None, "4,1":None, "4,2":None, "4,3":None,
                       "4,4":None, "4,5":None, "4,6":None, "4,7":None,
  
                       "5,0":None, "5,1":None, "5,2":None, "5,3":None,
                       "5,4":None, "5,6":None, "5,7":None, "5,8":None,
  
                       "6,0":"pion-n", "6,1":"pion-n", "6,2":"pion-n", "6,3":"pion-n",
                       "6,4":"pion-n", "6,5":"pion-n", "6,6":"pion-n", "6,7":"pion-n",
  
                       "7,0":"tourG-n", "7,1":"cavalierG-n", "7,2":"fouG-n", "7,3":"dame-n",
                       "7,4":"roi-n", "7,5":"fouD-n", "7,6":"cavalierD-n", "7,7":"tourD-n"
                       }
                          
        self.case = ''.join(self.plateau.keys()) #Toutes les cases de l'échiquier                     
        
 
    def updatePlateau(self):
        """Met à jour le plateau"""
        self.newPlateau = self.bougerPiece() #ou p?
        self.plateau = self.newPlateau
  
