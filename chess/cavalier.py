#! c:/Python33 python
# -*- coding:Utf-8 -*-

"""
    @file: cavalier.py
    @author:  Zoe Tolszczuk-Leclerc
    
    Fichier contenant la classe Cavalier
"""

from chess.piece import Piece
class Cavalier(Piece):
    """Un cavalier est une pièce d'échec qui peut se déplacer selon un L soit une dans une orientation et deux dans une autre"""
    
    def __init__(self,line,col,couleur):
        """Initialise un cavalier à la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        Piece.__init__(self,line,col,couleur)
    
    def posFuturesPossibles(self,plateau):
        lf = []
        cavpos = [[self.pos[0]+1,self.pos[1]+2],[self.pos[0]+2,self.pos[1]+1],[self.pos[0]+2,self.pos[1]-1],[self.pos[0]+1,self.pos[1]-2],[self.pos[0]-1,self.pos[1]-2],[self.pos[0]-2,self.pos[1]-1],[self.pos[0]-2,self.pos[1]+1],[self.pos[0]-1,self.pos[1]+2]]
        for l in cavpos:
            if plateau.getPiece(l[0],l[1]) != None:
                if plateau.getPiece(l[0],l[1]).color == self.color:
                    break
                else:
                    lf.append(l)
                    break
            else:
                lf.append(l)
        return lf

    def deplacer(self,nouvPos,plateau):
        if nouvPos in self.posFuturesPossibles(plateau):
            self.pos = nouvPos
        else:
            return self.pos# else on ne change rien : on retourne la position courante
        # pour signifier que le changement a eu lieu ... ou pas
    
    def __repr__(self):
        if self.color == 0:
            return str(self.pos[0])+str(self.pos[1])+"CN"
        else:
            return str(self.pos[0])+str(self.pos[1])+"CB"


#-----------------
# FIN CLASSE CAVALIER
#-----------------

#-----------------
#Copie test tour camille pour en faire tes cavalier
#------------------

def test_pos():
    from chess.plateau import Plateau
    p = Plateau()
    cn1 = p.getPiece(0,1)
    cn2 = p.getPiece(0,6)
    cb1 = p.getPiece(7,1)
    cb2 = p.getPiece(7,6)
    
    print(p.damier)
    cn1.deplacer((2,2),p) # 0,0 -> 2,2 # Ok
    print(cn1)
    p.damier[(2,2)] = cn1
    p.damier.pop((0,1))
    
    cn2.deplacer((0,5),p) # 0,6 -> 0,5 # Ne fais rien / mouvement non autorisé
    cn2.deplacer((3,6),p) # 0,6 -> 3,6 # Ne fais rien / mouvement non autorisé
    print(cn2)
    cn2.deplacer((1,4),p) # 0,6 -> 1,4 # Ok
    print(cn2)
    p.damier[(1,4)] = cn2
    p.damier.pop((0,6))
    cn2.deplacer((3,5),p) # 1,4 -> 3,5 # Ok
    print(cn2)
    p.damier[(3,5)] = cn2
    p.damier.pop((1,4))
    cn2.deplacer((4,3),p) # 3,5 -> 4,3 # Ok
    print(cn2)
    p.damier[(4,3)] = cn2
    p.damier.pop((3,5))
    cn1.deplacer((4,3),p) # 2,2 -> 4,3 # Ne fais rien / cn2 a l'arrivee
    print(cn1)
    cb1.deplacer((6,0),p) # 7,1 -> 6,0 # ne fais rien / mouvement non autorisé
    print(cb1)
    cb1.deplacer((5,2),p) # 7,1 -> 5,2 # Ok
    print(cb1)
    p.damier[(5,2)] = cb1
    p.damier.pop((7,1))
    cb2.deplacer((6,4),p) # 7,6 -> 6,4 # Ok
    print(cb2)
    p.damier[(6,4)] = cb2
    p.damier.pop((7,6))
    cb2.deplacer((4,3),p) # 6,4 -> 4,3 # Cavalier blanc mange cavalier noire !
    print(cb2)
    p.damier[(4,3)] = cb2
    p.damier.pop((6,4))
    cn1.deplacer((4,3),p) # 2,2 -> 4,3 # Cn1 mange Cb2
    print(cn1)
    p.damier[(4,3)] = cn1
    p.damier.pop((2,2))
    cn1.deplacer((5,3),p) # 4,3 -> 5,3 # Ne fais rien / mouvement impossible
    print(cn1)
    cb1.deplacer((3,1),p) # 5,2 -> 3,1 # Ok
    print(cb1)
    p.damier[(5,2)] = cb1
    p.damier.pop((5,2))
    cn1.deplacer((3,1),p) # 4,3 -> 3,1 # Ok on mange cb1
    print(cn1)
    p.damier[(0,3)] = cn1
    p.damier.pop((4,3))
    print(p.damier)
    
    
    
if __name__ == "__main__":

    test_pos()
