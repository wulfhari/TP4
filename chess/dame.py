'''
Created on Nov 16, 2013

@author: Simon
'''
from chess.piece import Piece

class Dame(Piece):
    unicode_dameb='\u2655'

    """La reine est une piece d'echec qui peut se deplacer dans toutes les directions sans limites de cases. Ne peut passer par dessus une piece"""


    def __init__(self,line,col,couleur):
        """Initialise une dame a la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        Piece.__init__(self,line,col,couleur)

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
        x = nouvPos[0]-self.pos[0]
        y = nouvPos[1]-self.pos[1]
        # Si une piece a l'arrivee et identique a la couleur de la dame
        pieceArr = plateau.getPiece(pos_arr[0],pos_arr[1])
        if pieceArr != None and pieceArr.color == self.color:
            return False

        elif (pos_dep[0] == pos_arr[0]) :
            # Deplacement sur la meme ligne
            depart = min(pos_dep[1],pos_arr[1])+1
            arrivee = max(pos_dep[1],pos_arr[1])-1
            # Si une piece est sur le chemin, la dame ne peut pas passer
            for i in range(depart,arrivee):
                if plateau.getPiece(pos_dep[0],i) != None:
                    return False
            # Rendu ici, il n'y a pas de piece sur le chemin et la piece a l'arrivee
            # est de couleur differente s'il y'en a une.
            return True
        elif (pos_dep[1] == pos_arr[1]) :
            # Deplacement sur la meme colonne
            depart = min(pos_dep[0],pos_arr[0])+1
            arrivee = max(pos_dep[0],pos_arr[0])-1
            # Si une piece est sur le chemin, la dame ne peut pas passer
            for i in range(depart,arrivee):
                if plateau.getPiece(i,pos_dep[1]) != None:
                    return False
            # Rendu ici, il n'y a pas de piece sur le chemin et la piece a l'arrivee
            # est de couleur differente s'il y'en a une.
            return True
        elif y == 0:
            return False
        elif x%y == 0:
            i = 1
            # Deplacement sur la diagonale haut gauche
            if x>0 and y < 0:
                while i != x:
                    if plateau.getPiece(self.pos[0]+i, self.pos[1]-i) != None:
                        return False
                        # Si une piece est sur le chemin, la dame ne peut pas passer
                    else:
                        i = i+1
                return True
            # Deplacement sur la diagonale haut gauche
            elif x>0 and y > 0:
                while i != x:
                    if plateau.getPiece(self.pos[0]+i, self.pos[1]+i) != None:
                        return False
                        # Si une piece est sur le chemin, la dame ne peut pas passer
                    else:
                        i = i+1
                return True
            # Deplacement sur la diagonale haut gauche
            elif x<0 and y < 0:
                while i != x:
                    if plateau.getPiece(self.pos[0]-i, self.pos[1]-i) != None:
                        return False
                        # Si une piece est sur le chemin, la dame ne peut pas passer
                    else:
                        i = i+1
                return True
            # Deplacement sur la diagonale haut gauche
            elif x<0 and y >0:
                while i != x:
                    if plateau.getPiece(self.pos[0]-i, self.pos[1]+i) != None:
                        return False
                        # Si une piece est sur le chemin, la dame ne peut pas passer
                    else:
                        i = i+1
                return True
        else: # On a essaye autre chose que les lignes, les colonnes et les diagonales...
            return False

    def __repr__(self):
        if self.color == 0:
            return str(self.pos[0])+str(self.pos[1])+"DN"
        else:
            return str(self.pos[0])+str(self.pos[1])+"DB"

#-----------------
# FIN CLASSE DAME
#-----------------

def test_pos():
    from chess.plateau import Plateau
    p = Plateau()
    dn = p.getPiece(0,3)
    db = p.getPiece(7,3)

    print(p.damier)
    dn.deplacer((3,0),p) # 0,3 -> 3,0 # Ok
    print(dn)
    p.damier[(3,0)] = dn
    p.damier.pop((0,3))
    dn.deplacer((7,3),p) # 3,0 -> 7,3 # Ne fais rien / mouvement non autorisa
    dn.deplacer((4,2),p) # 3,0 -> 4,2 # Ne fais rien / mouvement non autorisa
    print(dn)
    dn.deplacer((3,1),p) # 3,0 -> 3,1 # Ok
    print(dn)
    p.damier[(3,1)] = dn
    p.damier.pop((3,0))
    db.deplacer((3,3),p) # 7,3 -> 3,3 # Ok
    print(db)
    p.damier[(3,3)] = db
    p.damier.pop((7,3))
    dn.deplacer((3,5),p) # 3,1 -> 3,5 # Ne fais rien / db dans le chemin
    print(dn)
    db.deplacer((3,0),p) # 3,3 -> 3,0 # Ne fais rien / dn dans le chemin
    print(db)
    dn.deplacer((5,3),p) # 3,1 -> 5,3 # Ok
    print(dn)
    p.damier[(5,3)] = dn
    p.damier.pop((3,1))
    db.deplacer((0,6),p) # 3,3 -> 0,6 # Ok
    print(db)
    p.damier[(0,6)] = db
    p.damier.pop((3,3))
    dn.deplacer((5,5),p) # 5,3 -> 5,5 # OK
    print(dn)
    p.damier[(5,5)] = dn
    p.damier.pop((5,3))
    db.deplacer((0,5),p) # 0,6 -> 0,5 # OK
    print(db)
    p.damier[(0,5)] = db
    p.damier.pop((0,6))
    dn.deplacer((0,6),p) # 5,5 -> 0,6 # Ne fais rien / mouvement impossible
    print(dn) 
    dn.deplacer((0,5),p) # 5,5 -> 0,5 # Ok / Dame noire mange dame blanche
    print(dn)
    p.damier[(0,5)] = dn
    p.damier.pop((5,5))
    print(p.damier)

if __name__ == "__main__":
    test_pos()