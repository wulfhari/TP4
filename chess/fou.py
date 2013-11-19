#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""     
Fichier contenant la classe Fou
 
+Created on Nov 13, 2013
@author: Claudine et Zoé
 
"""
from chess.piece import Piece
class Fou(Piece):
    """Un fou est une piece d'echec qui peut se deplacer en diagonale"""
 
    def __init__(self,line,col,couleur):
        """Initialise un fou a la position 'ligne,colonne' avec la bonne couleur 0 pour noir, 1 pour blanc"""
        Piece.__init__(self,line,col,couleur)
 
    def deplacer(self,nouvPos,plateau):
        if self.deplacementValide(nouvPos,plateau):
            plateau.damier[nouvPos] = self
            plateau.damier[self.pos] = None
            self.pos=nouvPos
            self.abouge=0
            
        return self.pos       
    def deplacementValide(self,nouvPos,plateau):
        x = nouvPos[0]-self.pos[0]
        y = nouvPos[1]-self.pos[1]
        
        if y == 0:  
            print("Coup invalide")
            return False
        if y == 0:
            return False
        if x % y == 0:
            pos_arr = nouvPos
            i = 1
            #Si une pièce à l'arrivée et identique à la couleur du fou
            pieceArr = plateau.getPiece(pos_arr[0],pos_arr[1])
            
            if pieceArr != None and pieceArr.color == self.color:
                return False
            
            #Deplacement sur la diagonale haut gauche
            elif x > 0 and y < 0:
                while i != x:
                    if plateau.getPiece(self.pos[0]+i, self.pos[1]-i) != None:
                        return False
                    # Si une pièce est sur le chemin, le fou ne peut pas passer
                    else:
                        i = i+1
                return True
            
            #Deplacement sur la diagonale haut gauche
            elif x > 0 and y > 0:
                while i != x:
                    if plateau.getPiece(self.pos[0]+i, self.pos[1]+i) != None:
                        return False
                    # Si une pièce est sur le chemin, le fou ne peut pas passer
                    else:
                        i = i+1
                return True
            
            #Deplacement sur la diagonale haut gauche
            elif x < 0 and y < 0:
                while i != x:
                    if plateau.getPiece(self.pos[0-i], self.pos[1]-i) != None:
                        return False
                        # Si une pièce est sur le chemin, le fou ne peut pas passer
                    else:
                        i = i+1
                return True
                                                 
            #Deplacement sur la diagonale haut gauche
            elif x < 0 and y > 0:
                while i != x:
                    if plateau.getPiece(self.pos[0]-i, self.pos[1]+i) != None:
                        return False
                        # Si une pièce est sur le chemin, le fou ne peut pas passer
                    else:
                        i = i+1
                return True
                     
        else:
            return False
  
        
    def __repr__(self):
        if self.color == 0:
            return str(self.pos[0])+str(self.pos[1])+"FN"
        else:
            return str(self.pos[0])+str(self.pos[1])+"FB"
     


#-----------------
# FIN CLASSE FOU
#-----------------

#------------------
#Copie test tour camille pour en faire test fou
#------------------

def test_pos():
    from chess.plateau import Plateau
    p = Plateau()
    fn1 = p.getPiece(0,2)
    fn2 = p.getPiece(0,5)
    fb1 = p.getPiece(7,2)
    fb2 = p.getPiece(7,5)
    
    print(p.damier)
    fn1.deplacer((1,2),p) # 0,2 -> 1,2 # Ne fait rien / mouvement non autorisé
    print(fn1)
    fn1.deplacer((1,3),p) # 0,2 -> 1,3 # Ok
    p.damier[(1,3)] = fn1
    p.damier.pop((0,2))    
    print(fn1)
    fn1.deplacer((0,4),p) # 1,3 -> 0,4 # Ok
    p.damier[(0,4)] = fn1
    p.damier.pop(1,3)
    print(fn1)
    fn1.deplacer((4,4),p) # 0,4 -> 4,4 # Ok
    print(fn1)
    p.damier[(4,4)] = fn1
    p.damier.pop((0,4))    
    
    fn2.deplacer((4,5),p) # 0,5 -> 4,5 # Ne fait rien / mouvement non autorisé
    fn2.deplacer((2,7),p) # 0,5 -> 2,7 # Ok
    p.damier[(2,7)] = fn1
    p.damier.pop((0,5)) 
    print(fn2)
    fn2.deplacer((6,3),p) # 2,7 -> 6,3 # Ok
    print(fn2)
    p.damier[(6,3)] = fn2
    p.damier.pop((2,7))    
    fn2.deplacer((7,3),p) # 6,3 -> 7,3 # Ne fait rien / mouvement non autorisé
    print(fn2)
        
    fb1.deplacer((6,0),p) # 7,2 -> 6,0 # ne fait rien / mouvement non autorisé
    print(fb1)
    fb1.deplacer((6,1),p) # 7,2 -> 6,1 # Ok
    print(fb1)
    p.damier[(6,1)] = fb1
    p.damier.pop((7,2))
    fb1.deplacer((4,3),p) # 6,1 -> 4,3 # Ok
    print(fb1)
    p.damier[(4,3)] = fb1
    p.damier.pop((6,1)) 
        
    fb2.deplacer((6,4),p) # 7,5 -> 6,4 # Ne fait rien / Pas même ligne et colonne
    print(fb2)
    fb2.deplacer((5,7),p) # 7,5 -> 5,7 # Ok
    print(fb2)
    p.damier[(5,7)] = fb2
    p.damier.pop((7,5)) 
    fb2.deplacer((5,5),p) # 5,7 -> 5,5 # Ne fait rien / Pas même ligne et colonne
    print(fb2)
    fb2.deplacer((3,5),p) # 5,7 -> 3,5 # Ok 
    print(fb2)
    p.damier[(3,5)] = fb2
    p.damier.pop((5,7)) 
    print(p.damier)
    
    
    
if __name__ == "__main__":

    test_pos()