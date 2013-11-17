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
    
    def deplacer(self,nouvPos,plateau):
        if self.deplacementValide(nouvPos,plateau):
            self.pos = nouvPos
        # else on ne change rien : on retourne la position courante
        # pour signifier que le changement a eu lieu ... ou pas
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
