'''
Created on Nov 16, 2013

@author: Simon
'''
from chess.piece import Piece
class Pion(Piece):
    '''
    Un pion peut se deplacer de deux cases a la vertical a son permier tour, se deplacer d'une case a la fois a la verticale et qui mange en diagonale
    '''
    
    def __init__(self,line,col,couleur):
        """Initialise un pion a la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        self.pos=(line,col)  # Sa position
        self.color=couleur   # sa couleur
        
    def deplacer(self,nouvPos,plateau):
        if self.deplacementValide(nouvPos,plateau)==True:
            self.pos=nouvPos
            self.abouge=0
        return self.pos
    
    def deplacementValide(self,nouvPos,plateau):
        pos_dep=self.pos
        pos_arr=nouvPos
        
        #Si une piece alliee est sur la case d'arrivee
        pieceArr=plateau.getPiece(pos_arr[0],pos_arr[1])
        pieceDev=plateau.getPiece(pos_dep[0]+1,pos_dep[1])  #Pour le saut de deux cases
        if (pieceArr != None) and (pieceArr.color == self.color) :
            return False
       
        #PIONS NOIRS
        
        if self.color==0:
            
            #Avancer de deux cases a son premier coup
            if (pos_dep[0]+2==pos_arr[0]) and (pos_dep[1]==pos_arr[1]) and (self.abouge==1) and pieceDev==None :
                return True
        
            #les pions avancent toujours d'une seule case
            if (pos_dep[0]+1 == pos_arr[0]):
            
                #Deplacement en ligne droite de 1 case            
                if (pos_dep[1]==pos_arr[1]) and pieceArr == None:
                    return True
            
                #Deplacement en diagonale pour manger une piece
                elif (pos_dep[1]==pos_arr[1]+1) and pieceArr != None:
                    return True
            
                elif (pos_dep[1]==pos_arr[1]-1) and pieceArr != None:
                    return True
            
                else:
                    return False
            
        #PIONS BLANCS
        
        if self.color==1:
            
            #Avancer de deux cases a son premier coup
            if (pos_dep[0]-2==pos_arr[0]) and (pos_dep[1]==pos_arr[1]) and (self.abouge==1) and pieceDev==None :
                return True
        
            #les pions avancent toujours d'une seule case
            if (pos_dep[0]-1 == pos_arr[0]):
            
                #Deplacement en ligne droite de 1 case            
                if (pos_dep[1]==pos_arr[1]) and pieceArr == None:
                    return True
            
                #Deplacement en diagonale pour manger une piece
                elif (pos_dep[1]==pos_arr[1]+1) and pieceArr != None:
                    return True
            
                elif (pos_dep[1]==pos_arr[1]-1) and pieceArr != None:
                    return True
            
                else:
                    return False
            

        else:
            return False
        
def test_pion():
    from chess.plateau import Plateau
    p = Plateau()
    pn1 = p.getPiece(1,0)
    pn2 = p.getPiece(1,1)
    pb1 = p.getPiece(6,0)
    pb2 = p.getPiece(6,1)
    
    print(p.damier)
    pn1.deplacer((2,0),p)
    pn2.deplacer((3,1),p)
    pb1.deplacer((4,0),p)
    pn2.deplacer((4,0),p) #pn2 mange pb1
    pb2.deplacer((5,1),p)
    pb2.deplacer((3,1),p) #invalide, avance de 2 a son 2ieme coup
    pn2.deplacer((5,1),p) #invalide, personne a manger
    
    
    

    


if __name__=="__main__":
    test_pion()