#! c:/Python33 python
# -*- coding:Utf-8 -*-

"""
@file: tour.py
@author:  C. Besse

Fichier contenant la classe Tour
"""

class Tour:
    """Une tour est une pièce d'échec qui peut se déplacer selon les ligne set les colonnes"""
    
    def __init__(self,line,col,couleur):
        """Initialise une tour à la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        pass
    
    def deplacer(self,n_line,n_col,plateau):
        pass

    def deplacementValide(self,pos_dep,pos_arr,plateau):
        pass
            

#-----------------
# FIN CLASSE TOUR
#-----------------

def test_pos():
        from chess.plateau import Plateau
        p = Plateau()
        tn1 = p.getPiece(0,0)
        tn2 = p.getPiece(0,7)
        tb1 = p.getPiece(7,0)
        tb2 = p.getPiece(7,7)
        
        print(tn1.deplacer(0,3,p))
        p.damier[(0,3)] = tn1
        p.damier.pop((0,0))
        print(tn2.deplacer(0,4,p)) 
        p.damier[(0,4)] = tn2
        p.damier.pop((0,7))
        print(tb1.deplacer(0,3,p)) # ne fais rien
        print(tb1.deplacer(0,0,p))
        p.damier[(0,0)] = tb1
        p.damier.pop((7,0))
        print(tb1.deplacer(0,3,p)) # On mange !
        p.damier[(0,3)] = tb1
        p.damier.pop((0,0)) 
        print(tn2.deplacer(0,3,p)) # On mange !
        p.damier[(0,3)] = tn2
        p.damier.pop((0,4)) 
        print(tb2.deplacer(0,3,p)) # Ne fais rien
        print(p.damier)
        
if __name__ == "__main__":
    
    test_pos()     
#    test_pos2()     
        
        
        
