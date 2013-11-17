#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""     
Fichier contenant la classe fou
 
+Created on Nov 13, 2013
@author: Claudine
 
"""

class Fou(Piece):
    """Un fou est une piece d'echec qui peut se deplacer en diagonale"""
 
    def __init__(self, line, col, couleur):
    """Initialise un fou a la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
    piece.__init__(self,line,col,couleur)
    
    def deplacementValide(self,nouvPos,plateau):
        x = nouvPos[0]-self.pos[0]
        y = nouvPos[1]-self.pos[1]
        
        if x%y == 0:
            
            pos_dep = self.pos
            pos_arr = nouvPos
            i = 1
            # Si une pièce à l'arrivée et identique à la couleur du fou
            pieceArr = plateau.getPiece(pos_arr[0],pos_arr[1])
            
            if pieceArr != None and pieceArr.color == self.color:
                return False
            
            # Deplacement sur la diagonale haut gauche
            elif x>0 and y < 0:
                while i != x:
                    if plateau.getPiece(self.pos[0]+i, self.pos[1]-i) != None:
                        return False
                    # Si une pièce est sur le chemin, le fou ne peut pas passer
                    else:
                        i = i+1
                return True
            
            # Deplacement sur la diagonale haut gauche
            elif x>0 and y > 0:
                while i != x:
                    if plateau.getPiece(self.pos[0]+i, self.pos[1]+i) != None:
                        return False
                    # Si une pièce est sur le chemin, le fou ne peut pas passer
                    else:
                        i = i+1

            # Deplacement sur la diagonale haut gauche
            elif x<0 and y < 0:
                while i != x:
                    if plateau.getPiece(self.pos[0-i, self.pos[1]-i) != None:
                        return False
                        # Si une pièce est sur le chemin, le fou ne peut pas passer
                    else:
                        i = i+1
                                                 
            # Deplacement sur la diagonale haut gauche
            elif x<0 and y >0:
                while i != x:
                    if plateau.getPiece(self.pos[0]-i, self.pos[1]+i) != None:
                        return False
                        # Si une pièce est sur le chemin, le fou ne peut pas passer
                    else:
                        i = i+1
                                                 
        else:
            return False
  
    def deplacer(self,nouvPos,plateau):
        if self.deplacementValide(nouvPos,plateau):
            self.pos = nouvPos
    # else on ne change rien : on retourne la position courante
    # pour signifier que le changement a eu lieu ... ou pas
            return self.pos
    
    def __repr__(self):
        """ Petit truc pour l'affichage """
        if self.color == 0:
            return "Fou Noire "+ str(self.pos)
        else:
            return "Fou Blanche"+ str(self.pos)

    

#-----------------
# FIN CLASSE FOU
#-----------------

#------------------
#Copie test tour camille pour en faire test fou
#------------------

def test_pos():
    from plateau import Plateau
    p = Plateau()
    fn1 = p.getPiece(0,2)
    fn2 = p.getPiece(0,5)
    fb1 = p.getPiece(7,2)
    fb2 = p.getPiece(7,5)
    
    print(p.damier)
    fn1.deplacer((1,3),p) # 0,2 -> 1,3 # Ok
    print(fn1)
    p.damier[(1,3)] = fn1
    p.damier.pop((0,2))
    
    fn2.deplacer((1,5),p) # 0,5 -> 1,5 # Ne fais rien / mouvement non autorisé
    fn2.deplacer((3,5),p) # 0,5 -> 3,5 # Ne fais rien / mouvement non autorisé
    print(cn2)
    fn2.deplacer((1,4),p) # 0,5 -> 1,4 # Ok
    print(fn2)
    p.damier[(1,4)] = fn2
    p.damier.pop((0,5))
    
    
    fn2.deplacer((3,5),p) # 1,4 -> 3,5 # Ok
    print(fn2)
    p.damier[(3,5)] = fn2
    p.damier.pop((1,4))
    fn2.deplacer((4,3),p) # 3,5 -> 4,3 # Ok
    print(fn2)
    p.damier[(4,3)] = fn2
    p.damier.pop((3,5))
    fn1.deplacer((4,3),p) # 2,2 -> 4,3 # Ne fais rien / cn2 a l'arrivee
    print(cnf)
    fb1.deplacer((6,0),p) # 7,1 -> 6,0 # ne fais rien / mouvement non autorisé
    print(fb1)
    fb1.deplacer((5,2),p) # 7,1 -> 5,2 # Ok
    print(cb1)
    p.damier[(5,2)] = fb1
    p.damier.pop((7,1))
    fb2.deplacer((6,4),p) # 7,6 -> 6,4 # Ok
    print(fb2)
    p.damier[(6,4)] = fb2
    p.damier.pop((7,6))
    fb2.deplacer((4,3),p) # 6,4 -> 4,3 # Cavalier blanc mange cavalier noire !
    print(fb2)
    p.damier[(4,3)] = fb2
    p.damier.pop((6,4))
    fn1.deplacer((4,3),p) # 2,2 -> 4,3 # Cn1 mange Cb2
    print(fn1)
    p.damier[(4,3)] = fn1
    p.damier.pop((2,2))
    fn1.deplacer((5,3),p) # 4,3 -> 5,3 # Ne fais rien / mouvement impossible
    print(fn1)
    fb1.deplacer((3,1),p) # 5,2 -> 3,1 # Ok
    print(fb1)
    p.damier[(5,2)] = fb1
    p.damier.pop((5,2))
    fn1.deplacer((3,1),p) # 4,3 -> 3,1 # Ok on mange cb1
    print(fn1)
    p.damier[(0,3)] = fn1
    p.damier.pop((4,3))
    print(p.damier)
    
    
    
if __name__ == "__main__":

    test_pos()