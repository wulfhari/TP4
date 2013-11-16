#! c:/Python33 python
# -*- coding:Utf-8 -*-

"""
    @file: fou.py
    @author:  Claudine Laurendeau
    
    Fichier contenant la classe fou


Created on Nov 13, 2013
@author: Claudine

"""
from chess.piece import Piece
class fou(Piece):
    
    # Un fou est une piece d'echec qui peut se deplacer en diagonale

    def __init__(self, line, col, couleur):
        '''
        """Initialise un cavalier a la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        '''
        self.line = line
        self.col = col
        self.couleur = couleur
        
    
    def deplacer(self,n_line,n_col,plateau):
        if deplacementValide == True:
            #code ici pour effecturer le deplacement
            pos_arr = pos_dep
        else:
            #Code ici si on peut pas faire le d�placement, ou d�placement non autoris�... est-ce ici qu'on envoie le message d'erreur et relance la fonction --> nextturn()
    
    def deplacementValide(self,nouvPos,plateau):
        pos_dep = self.pos 
        pos_arr = nouvPos #input joueur de next turn()??? semble �tre une liste
        #Si une piece a� l'arrivee est identique
        pieceArr = plateau.getPiece(pos_arr[0],pos_arr[1])
        if pieceArr != None and pieceArr.color == self.color:
            return False
        #Deplacement sur la meme ligne
        if (pos_dep[0] == pos_arr[0]):
            depart = min(pos_dep[1],pos_arr[1])+1
            arrivee = max(pos_dep[1],pos_arr[1])-1
            #si une piece est dans le chemin
            for i in range(depart,arrivee):
                if plateau.get.Piece(pos_dep[0],i) |- None:
                    return False
            return True
        
        elif ... pour la colone        
        

