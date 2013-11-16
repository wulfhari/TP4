#! c:/Python33 python
# -*- coding:Utf-8 -*-

"""
    @file: king.py
    @author:  Zoe Tolszczuk-Leclerc
    
    Fichier contenant la classe king
    """"


class king(Piece):
    """Le Roi est une pièce d'échec qui peut se déplacer dans toutes les directions (comme la reine), mais d'une seule case à la fois"""
    
    def __init__(self,line,col,couleur):
        """Initialise un roi à la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        Piece.__init__(self,line,col,couleur)
    
    def deplacer(self,n_line,n_col,plateau):
        if deplacementValide == True:
        #code ici pour effecturer le deplacement
        else:
    #Code ici si on peut pas faire le deplacement, ou déplacement non autorise... est-ce ici qu'on envoie le message d'erreur et relance la fonction --> nextturn()
    
    def posFuturesPossibles(self,plateau):
        
        lf = []
        cavpos = [[self.pos[0]+1,self.pos[1]-1],[self.pos[0],self.pos[1]-1],[self.pos[0]-1,self.pos[1]-1],[self.pos[0]-1,self.pos[1]],[self.pos[0]-1,self.pos[1]+1],[self.pos[0],self.pos[1]+1],[self.pos[0]+1,self.pos[1]+1],[self.pos[0]+1,self.pos[1]]]
        for l in cavpos:
            if Piece != None:
                if Piece.color == self.color:
                    break
                else:
                    append.lf(l)
                    break
            else:
                append.lf()
    
    def deplacer(self,nouvPos,plateau):
        if nouvPos in self.posFuturesPossibles(plateau):
            self.pos = nouvPos
        # else on ne change rien : on retourne la position courante
        # pour signifier que le changement a eu lieu ... ou pas
        return self.pos
    
    def __repr__(self):
        """ Petit truc pour l'affichage """
        if self.color == 0:
            return "Roi Noir "+str(self.pos)
        else:
            return "Roi Blanc"+str(self.pos)


#-----------------
# FIN CLASSE CAVALIER
#-----------------

#-----------------
#Copie test tour camille pour en faire tes cavalier
#------------------

def test_pos():
    from plateau import Plateau
    p = Plateau()
    rn = p.getPiece(0,4)
    rb = p.getPiece(7,4)
    
    print(p.damier)
    rn.deplacer((1,4),p) # 0,4 -> 1,4 # Ok
    print(rn)
    p.damier[(1,4)] = cn1
    p.damier.pop((0,4))
    rb.deplacer((6,6),p) # 7,4 -> 6,6 # Ne fais rien / mouvement non autorisé
    rb.deplacer((1,4),p) # 7,4 -> 1,4 # Ne fais rien / mouvement non autorisé
    print(rb)
    rb.deplacer((6,4),p) # 7,4 -> 6,4 # Ok
    print(rb)
    p.damier[(6,4)] = rb
    p.damier.pop((7,4))
    rn.deplacer((2,3),p) # 1,4 -> 2,3 # Ok
    print(rn)
    p.damier[(2,3)] = cn2
    p.damier.pop((1,4))
    rb.deplacer((5,3),p) # 6,4 -> 5,3 # Ok
    print(rb)
    p.damier[(5,3)] = rb
    p.damier.pop((6,4))
    rn.deplacer((5,0),p) # 2,3 -> 5,0 # Ne fais rien / pas plus d'une case à la fois possible
    print(rn)
    rn.deplacer((3,4),p) # 2,3 -> 3,4 # Ok
    print(rn)
    p.damier[(3,4)] = rn
    p.damier.pop((2,3))
    rb.deplacer((5,2),p) # 5,3 -> 5,3 # Ok
    print(rb)
    p.damier[(5,2)] = rb
    p.damier.pop((5,3))
    rn.deplacer((3,5),p) # 3,4 -> 3,5 # Ok
    print(rn)
    p.damier[(3,5)] = rn
    p.damier.pop((3,4))
    rb.deplacer((4,3),p) # 5,2 -> 4,3 # Ok
    print(rb)
    p.damier[(4,3)] = rb
    p.damier.pop((5,2))
    rn.deplacer((4,3),p) # 3,5 -> 4,3 # Ne fais rien / mouvement impossible
    print(rn)
    rn.deplacer((4,5),p) # 3,5 -> 4,3 # Ok
    print(rn)
    p.damier[(4,5)] = rn
    p.damier.pop((3,5))
    rb.deplacer((4,5),p) # 4,3 -> 4,5 # Ne fais rien / ne peut sauter deux cases
    print(rb)
    rb.deplacer((5,4),p) # 4,3 -> 5,4 # Ok
    print(rb)
    p.damier[(5,4)] = rb
    p.damier.pop((4,3))
    rn.deplacer((5,4),p) # 4,5 -> 5,4 # Ok Roi noir mange roi blanc
    print(rn)
    p.damier[(5,4)] = rn
    p.damier.pop((4,5))
    
    print(p.damier)


if __name__ == "__main__":
    
    test_pos()