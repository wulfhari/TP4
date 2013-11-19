#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Pour No suicide

Voir si on bonge le roi, les autres pieces peuvent le manger

!!!!!!Si piece jouer ROI!!!!!!

Donc poser posR comme nouv pos Roi (donc Input du joueur) dans fonction echec

!!!!!Si autre piece qui est joue!!!!!

Voir si une fois le deplacement effectue le roi peut se faire manger 

donc effectuer deplacer
nouveau damier
echec dans nouveau damier
si echec  == True
No suicide == True



board.damier[(int(user_input[0]),int(user_input[1]))].deplacer((int(user_input[2]),int(user_input[3])), board)
'''
def no_suicide(self,user_input,board):
    from chess.plateau import Plateau
    from chess.tour import Tour
    from chess.dame import Dame
    from chess.roi import Roi
    from chess.pion import Pion
    from chess.fou import Fou
    from chess.cavalier import Cavalier
    from chess.gamemanagement import GameManagement

    f = board.damier.values() 
    
    #Pour quand le roi est deplace
    for i in board.damier[(int(user_input[0]),int(user_input[1]))]:
        i = str(i)
        if i[2] == "R":
            lsp = []
            pk = []
            posR = [(int(user_input[2]),int(user_input[3]))]
            #quel couleur de piece devons nous chercher
            if self.alternance(board) == 'Noir':
                m = 'B'
            elif self.alternance(board) == 'Blanc':
                m = 'N'   
            #Pour recuperer en liste l'emplacement des pieces 'roi et/ou cavalier' de couleur adverse sur le damier
            for j in f:
                if j != None:
                    j = str(j)
                    if j[2] == "C"+m:
                        lsp.append(int(j[0]),int(j[1]))
                    elif j[2] == "R"+m:
                        lsp.append(int(j[0]),int(j[1]))
            #Pour recuperer en liste l'emplacement des pieces 'pion,tour,dame et fou' de couleur adverse sur le damier
            for k in f:
                if k != None:
                    k = str(k)
                    if k[2] == "P"+m:
                        pk.append(int(k[0]),int(k[1]))
                    elif k[2] == "T"+m:
                        pk.append(int(k[0]),int(k[1]))
                    elif k[2] == "D"+m:
                        pk.append(int(k[0]),int(k[1]))
                    elif k[2] == "F"+m:
                        pk.append(int(k[0]),int(k[1]))  
            #Pour chaque roi ou cavalier adverse est-ce que le roi est dans leur liste de position possibles
            for l in lsp:
                if posR in board.damier[l].posFuturesPossibles():
                    return True   
            #Pour chaque pion, tour, dame ou fou adverse est-ce que le roi est dans un de leur deplacement valide
            for h in pk:
                if board.damier[h].deplacementValide(posR, board) == True:
                    return True
            else:
                return False    
        #Pour quand une piece autre que roi est deplacee    
        else:
            board_2 = board.damier
            board.damier[(int(user_input[0]),int(user_input[1]))].deplacer((int(user_input[2]),int(user_input[3])), board_2)
            board_2.echec(board_2)


