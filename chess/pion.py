'''
Created on Nov 16, 2013

@author: Simon
'''
from chess.piece import Piece
class Pion(Piece):
    '''
    classdocs
    '''    
    def __init__(self,line,col,couleur):
        """Initialise un roi � la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        self.pos=(line,col)  # Sa position
        self.color=couleur   # sa couleur
        
    def deplacer(self,nouvPos,plateau):
        if self.deplacementValide(nouvPos,plateau)==True:
            self.pos=nouvPos
        return self.pos
    
    def deplacementValide(self,nouvPos,plateau):
        pos_dep=self.pos
        pos_arr=nouvPos
        
        #Si une piece est sur la case d'arrivee
        pieceArr=plateau.getPiece(pos_arr[0],pos_arr[1])
        if (pieceArr != None) and (pieceArr.color == self.color) :
            return False
        
        ###a revoir, fonctionne juste pour l'equipe qui doit monter        
        #le pion avance toujours d'une ligne
        if (pos_dep[0]+1 == pos_arr[0]):
            
        #Deplacement en ligne droite de 1 case            
            if (pos_dep[1]==pos_arr[1]) and pieceArr == None:
                return True
            
        #Deplacement en diagonale pour manger une piece
            elif (pos_dep[1]==pos_arr[1]+1) and pieceArr != None:
                return True
            
            elif (pos_dep[1]==pos_arr[1]-1) and pieceArr != None:
                return True
            
            else:
                return False
        
        else:
            return False

