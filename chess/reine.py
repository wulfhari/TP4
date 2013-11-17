"""
    @file: reine.py
    @author:  Zoe Tolszczuk-Leclerc
    
    Fichier contenant la classe Reine
    """

from chess.piece import Piece
class Reine(Piece):
    """La reine est une pièce d'échec qui peut se déplacer dans toutes les directions sans limites de cases. Ne peut passer par dessus une pièce"""
    
    def __init__(self,line,col,couleur):
        """Initialise une reine à la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        Piece.__init__(self,line,col,couleur)
    
    def posFuturesPossibles(self,plateau):
        lf = []
        cavpos = [[self.pos[0]+1,self.pos[1]+2],[self.pos[0]+2,self.pos[1]+1],[self.pos[0]+2,self.pos[1]-1],[self.pos[0]+1,self.pos[1]-2],[self.pos[0]-1,self.pos[1]-2],[self.pos[0]-2,self.pos[1]-1],[self.pos[0]-2,self.pos[1]+1],[self.pos[0]-1,self.pos[1]+2]]
        for l in cavpos:
            if Piece != None:
                if Piece.color == self.color:
                    break
                else:
                    append.lf(l)
                    break
            else:
                append.lf()
        return lf
    
    def deplacer(self,nouvPos,plateau):
        if nouvPos in self.posFuturesPossibles(plateau):
            self.pos = nouvPos
        # else on ne change rien : on retourne la position courante
        # pour signifier que le changement a eu lieu ... ou pas
        return self.pos
    
    def __repr__(self):
        """ Petit truc pour l'affichage """
        if self.color == 0:
            return "Cavalier Noir"+str(self.pos)
        else:
            return "Cavalier Blanc"+str(self.pos)


#-----------------
# FIN CLASSE CAVALIER
#-----------------
