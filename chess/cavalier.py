#! c:/Python33 python
# -*- coding:Utf-8 -*-

"""
    @file: cavalier.py
    @author:  Zoe Tolszczuk-Leclerc
    
    Fichier contenant la classe Cavalier
    """"


class cavalier(piece):
    """Un cavalier est une pièce d'échec qui peut se déplacer selon un L soit une dans une orientation et deux dans une autre"""
    
    def __init__(self,line,col,couleur):
        """Initialise un cavalier à la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        piece.__init__(self,line,col,couleur)
    
    def deplacer(self,n_line,n_col,plateau):
        if deplacementValide == True:
            #code ici pour effecturer le deplacement
        else:
            #Code ici si on peut pas faire le deplacement, ou déplacement non autorise... est-ce ici qu'on envoie le message d'erreur et relance la fonction --> nextturn()

    def posFuturesPossibles(self,plateau):
        lf = []
        cavpos = [[self.pos[0]+1,self.pos[1]+2],[self.pos[0]+2,self.pos[1]+1],[self.pos[0]+2,elf.pos[1]-1],[self.pos[0]+1,self.pos[1]-2],[self.pos[0]-1,self.pos[1]-2],[self.pos[0]-2,self.pos[1]-1],[self.pos[0]-2,self.pos[1]+1],[self.pos[0]-1,self.pos[1]+2]]
        for l in cavpos:
            if piece != None:
                if piece.color == self.color:
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
            return "Cavalier Noire "+str(self.pos)
        else:
            return "Cavalier Blanche"+str(self.pos)


#-----------------
# FIN CLASSE CAVALIER
#-----------------