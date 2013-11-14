#! /usr/bin/env python
# -*- coding:Utf-8 -*-

"""
@file: Tour.py
@author:  C. Besse

Fichier contenant la classe Tour
"""

class Tour:
    """Une tour est une pièce d'échec qui peut se déplacer selon les ligne set les colonnes"""
    
    def __init__(self,line,col,couleur):
        """Initialise une tour à la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        self.pos = (line,col) # Sa position
        self.color = couleur # Sa couleur ... il faudra mettre super() si on a une classe Pièce mère.
        
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
            
    ###
    ###
    ### AUTRE SOLUTION, vous pouvez leur donner les deux.
    ###
    ###
    
    def posFuturesPossibles(self,plateau):
        lf = [] # Liste des positions futures possibles
        # Position au dessus de la position courante
        for l in reversed(range(0,self.pos[0])): #### VOIR REVERSED !
            piece = plateau.getPiece(l,self.pos[1])
            if piece != None:
                if piece.color == self.color:
                    break
                else:
                    lf += [(l,self.pos[1])]
                    break
            else:
                lf += [(l,self.pos[1])]
        # Position au dessous de la position courante
        for l in range(self.pos[0]+1,7):
            piece = plateau.getPiece(l,self.pos[1])
            if piece != None:
                if piece.color == self.color:
                    break
                else:
                    lf += [(l,self.pos[1])]
                    break
            else:
                lf += [(l,self.pos[1])]
                
        # Position à gauche de la position courante
        for c in reversed(range(0,self.pos[1])):#### VOIR REVERSED !
            piece = plateau.getPiece(self.pos[0],c)
            if piece != None:
                if piece.color == self.color:
                    break
                else:
                    lf += [(self.pos[0],c)]
                    break
            else:
                lf += [(self.pos[0],c)]
        # Position à droite de la position courante
        for c in range(self.pos[1]+1,7):
            piece = plateau.getPiece(self.pos[0],c)
            if piece != None:
                if piece.color == self.color:
                    break
                else:
                    lf += [(self.pos[0],c)]
                    break
            else:
                lf += [(self.pos[0],c)]

        # Quand on a fait les 4 côtés on renvoie la 
        # liste des positions futures possibles
        return lf
    
    def deplacer2(self,nouvPos,plateau):
        if nouvPos in self.posFuturesPossibles(plateau):
            self.pos = nouvPos
        # else on ne change rien : on retourne la position courante 
        # pour signifier que le changement a eu lieu ... ou pas
        return self.pos
    
    def __repr__(self):
        """ Petit truc pour l'affichage """
        if self.color == 0:
            return "Tour Noire "+str(self.pos)
        else:
            return "Tour Blanche"+str(self.pos)
        
#-----------------
# FIN CLASSE TOUR
#-----------------

def test_pos():
        from plateau import Plateau
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
        
def test_pos2():
        from plateau import Plateau
        p = Plateau()
        tn1 = p.getPiece(0,0)
        tn2 = p.getPiece(0,7)
        tb1 = p.getPiece(7,0)
        tb2 = p.getPiece(7,7)
        
        print(p.damier)
        tn1.deplacer2((0,3),p) # 0,0 -> 0,3 # Ok
        print(tn1)
        p.damier[(0,3)] = tn1
        p.damier.pop((0,0))
        tn2.deplacer2((0,1),p) # 0,7 -> 0,1 # Ne fais rien / tn1 dans le chemin
        tn2.deplacer2((0,1),p) # 0,7 -> 0,3 # Ne fais rien / tn1 à l'arrivée
        print(tn2)
        tn2.deplacer2((0,4),p) # 0,7 -> 0,4 # Ok
        print(tn2)
        p.damier[(0,4)] = tn2
        p.damier.pop((0,7))
        tb1.deplacer2((0,3),p) # 7,0 -> 0,3 # ne fais rien / Pas même ligne et colonne
        print(tb1)
        tb1.deplacer2((0,0),p) # 7,0 -> 0,0 # Ok
        print(tb1)
        p.damier[(0,0)] = tb1
        p.damier.pop((7,0))
        tb1.deplacer2((0,3),p) # 0,0 -> 0,3 # Tour blanche mange tour noire !
        print(tb1)
        p.damier[(0,3)] = tb1
        p.damier.pop((0,0)) 
        tn2.deplacer2((0,3),p) # 0,4 -> 0,3 # Ok on mange à une seule case de distance horizontale
        print(tn2)
        p.damier[(0,3)] = tn2
        p.damier.pop((0,4)) 
        tb2.deplacer2((0,3),p) # 7,7 -> 0,3 # Ne fais rien / Pas même ligne et colonne
        print(tb2)
        tb2.deplacer2((7,3),p) # 7,7 -> 7,3 # Ok
        print(tb2)
        p.damier[(7,3)] = tb2
        p.damier.pop((7,7)) 
        tb2.deplacer2((1,3),p) # 7,3 -> 1,3 # Ok
        print(tb2)
        p.damier[(1,3)] = tb2
        p.damier.pop((7,3)) 
        tb2.deplacer2((0,3),p) # 1,3 -> 0,3 # Ok on mange à une seule case de distance verticale
        print(tb2)
        p.damier[(0,3)] = tb2
        p.damier.pop((1,3)) 
        print(p.damier)
        
   
if __name__ == "__main__":
    
    test_pos()     
    test_pos2()     
        
        
        
