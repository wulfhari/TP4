#! c:/Python33 python
# -*- coding:Utf-8 -*-

"""
    @file: cavalier.py
    @author:  Zoe Tolszczuk-Leclerc
    
    Fichier contenant la classe Cavalier
    """"


class cavalier:
    """Un cavalier est une pièce d'échec qui peut se déplacer selon un L soit une dans une orientation et deux dans une autre"""
    
    def __init__(self,line,col,couleur,pos):
        """Initialise un cavalier à la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        Piece.__init__(self,line,col,couleur)
    
    def deplacer(self,n_line,n_col,plateau):
        if deplacementValide == True:
    
    
    def deplacementValide(self,nouvPos,plateau):
        pos_dep = self.pos
        pos_arr = nouvPos
        #Si une piece a  l'arrivee est identique
        pieceArr = plateau.getPiece(pos_arr[0],pos_arr[1])
        if pieceArr != None and pieceArr.color == self.color:
            return False
        #Deplacement sur la meme ligne
        if (pos_dep[0] == pos_arr[0]):
            depart = min(pos_dep[1],pos_arr[1])+1
            arrivee = max(pos_dep[1],pos_arr[1])-1
            #si une piece est dans le chemin
            for i in range(depart,arrivee):
                if plateau.get.Piece(pos_dep[0],i) |- None:
                    return False
            return True
        
        elif ... pour la colone
#-----------------
# FIN CLASSE CAVALIER
#-----------------