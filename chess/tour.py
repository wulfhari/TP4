#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""
@file: Tour.py
@author:  C. Besse

Fichier contenant la classe Tour
"""
from chess.piece import Piece
class Tour(Piece):
    """Une tour est une pièce d'échec qui peut se déplacer selon les ligne set les colonnes"""
    
    def __init__(self,line,col,couleur):
        """Initialise une tour à la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        self.pos = (line,col) # Sa position
        self.color = couleur # Sa couleur ... il faudra mettre super() si on a une classe Pièce mère.
        
    def deplacer(self,nouvPos,plateau):
        if self.deplacementValide(nouvPos,plateau):
            plateau.damier[nouvPos] = self
            plateau.damier[self.pos] = None
            self.pos=nouvPos
            self.abouge=0
            
        return self.pos     
        

    def deplacementValide(self,nouvPos,plateau):
        pos_dep = self.pos
        pos_arr = nouvPos 
        # Si une pièce à l'arrivée et identique à la couleur de la tour
        pieceArr = plateau.getPiece(pos_arr[0],pos_arr[1])
        if pieceArr != None and pieceArr.color == self.color:
            return False
        # Deplacement sur la même ligne 
        if (pos_dep[0] == pos_arr[0]) : 
            depart = min(pos_dep[1],pos_arr[1])+1
            arrivee = max(pos_dep[1],pos_arr[1])-1
            # Si une pièce est sur le chemin, la tour ne peut pas passer
            for i in range(depart,arrivee):
                if plateau.getPiece(pos_dep[0],i) != None:
                    return False
            # Rendu ici, il n'y a pas de pièce sur le chemin et la pièce à l'arrivée 
            # est de couleur différente s'il y'en a une.
            return True
        # Deplacement sur la même colonne 
        elif (pos_dep[1] == pos_arr[1]) : 
            depart = min(pos_dep[0],pos_arr[0])+1
            arrivee = max(pos_dep[0],pos_arr[0])-1
            # Si une pièce est sur le chemin, la tour ne peut pas passer
            for i in range(depart,arrivee):
                if plateau.getPiece(i,pos_dep[1]) != None:
                    return False
            # Rendu ici, il n'y a pas de pièce sur le chemin et la pièce à l'arrivée 
            # est de couleur différente s'il y'en a une.
            return True
        else: # On a essayé autre chose que les lignes et les colonnes ...
            return False

    
    def __repr__(self):
        if self.color == 0:
            return str(self.pos[0])+str(self.pos[1])+"TN"
        else:
            return str(self.pos[0])+str(self.pos[1])+"TB"

#-----------------
# FIN CLASSE TOUR
#-----------------

def test_pos():
    from chess.plateau import Plateau
    p = Plateau()
    tn1 = p.getPiece(0,0)
    tn2 = p.getPiece(0,7)
    tb1 = p.getPiece(7,0)
    tb2 = p.getPiece(7,7)
    
    print(p.damier)
    tn1.deplacer((0,3),p) # 0,0 -> 0,3 # Ok
    print(tn1)
    p.damier[(0,3)] = tn1
    p.damier.pop((0,0))
    tn2.deplacer((0,1),p) # 0,7 -> 0,1 # Ne fais rien / tn1 dans le chemin
    tn2.deplacer((0,1),p) # 0,7 -> 0,3 # Ne fais rien / tn1 à l'arrivée
    print(tn2)
    tn2.deplacer((0,4),p) # 0,7 -> 0,4 # Ok
    print(tn2)
    p.damier[(0,4)] = tn2
    p.damier.pop((0,7))
    tb1.deplacer((0,3),p) # 7,0 -> 0,3 # ne fais rien / Pas même ligne et colonne
    print(tb1)
    tb1.deplacer((0,0),p) # 7,0 -> 0,0 # Ok
    print(tb1)
    p.damier[(0,0)] = tb1
    p.damier.pop((7,0))
    tb1.deplacer((0,3),p) # 0,0 -> 0,3 # Tour blanche mange tour noire !
    print(tb1)
    p.damier[(0,3)] = tb1
    p.damier.pop((0,0)) 
    tn2.deplacer((0,3),p) # 0,4 -> 0,3 # Ok on mange à une seule case de distance horizontale
    print(tn2)
    p.damier[(0,3)] = tn2
    p.damier.pop((0,4)) 
    tb2.deplacer((0,3),p) # 7,7 -> 0,3 # Ne fais rien / Pas même ligne et colonne
    print(tb2)
    tb2.deplacer((7,3),p) # 7,7 -> 7,3 # Ok
    print(tb2)
    p.damier[(7,3)] = tb2
    p.damier.pop((7,7)) 
    tb2.deplacer((1,3),p) # 7,3 -> 1,3 # Ok
    print(tb2)
    p.damier[(1,3)] = tb2
    p.damier.pop((7,3)) 
    tb2.deplacer((0,3),p) # 1,3 -> 0,3 # Ok on mange à une seule case de distance verticale
    print(tb2)
    p.damier[(0,3)] = tb2
    p.damier.pop((1,3)) 
    print(p.damier)
                
   
if __name__ == "__main__":
    test_pos()     
    
        
        
        
