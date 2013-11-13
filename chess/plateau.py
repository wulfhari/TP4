#! c:/Python33 python
# -*- coding:Utf-8 -*-

"""
@file: plateau.py
@author:  C. Besse

from chess.tour import Tour

class Plateau:
    
    def __init__(self):
        """Initialise le plateau avec un damier vide"""
        self.damier = {(0,0):Tour(0,0,0), (0,7):Tour(0,7,0), (7,0):Tour(7,0,1), (7,7):Tour(7,7,1)}
        
    def getPiece(self,line,col):
        """Retourne la piece à la position (line,col) ou None sinon"""
        pass
"""

from chess import *
 
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
                       (0,0):tour(0,0,0), (0,1):cavalier(0,1,0), (0,2):fou(0,2,0), (0,3):dame(0,3,0),(0,4):roi(0,4,0), (0,5):four(0,5,0), (0,6):cavalier(0,6,0), (0,7):tour(0,7,0),
                       (1,0):pion(1,0,0), (1,1):pion(1,1,0), (1,2):pion(1,2,0), (1,3):pion(1,3,0),(1,4):pion(0,4,0), (1,5):pion(0,5,0), (1,6):pion(0,6,0), (1,7):pion(7,7,0),
                       (2,0):None, (2,1):None, (2,2):None, (2,3):None,(2,4):None, (2,5):None, (2,6):None, (2,7):None,
                       (3,0):None, (3,1):None, (3,2):None, (3,3):None,(3,4):None, (3,5):None, (3,6):None, (3,7):None,
                       (4,0):None, (4,1):None, (4,2):None, (4,3):None,(4,4):None, (4,5):None, (4,6):None, (4,7):None,
                       (5,0):None, (5,1):None, (5,2):None, (5,3):None,(5,4):None, (5,5):None, (5,6):None, (5,7):None,
                       (6,0):pion(6,0,1), (6,1):pion(6,1,1), (6,2):pion(6,2,1), (6,3):pion(6,3,1),(6,4):pion(0,4,1), (6,5):pion(0,5,1), (6,6):pion(0,6,1), (6,7):pion(7,7,1),
                       (7,0):tour(7,0,1), (7,1):cavalier(7,1,1), (7,2):fou(7,2,1), (7,3):dame(7,3,1),(7,4):roi(7,4,1), (7,5):four(7,5,1), (7,6):cavalier(7,6,1), (7,7):tour(7,7,1),
                       }
                          
        self.case = ''.join(self.plateau.keys()) #Toutes les cases de l'échiquier                     
        
 
    def updatePlateau(self):
        """Met à jour le plateau"""
        self.newPlateau = self.bougerPiece() #ou p?
        self.plateau = self.newPlateau
  
