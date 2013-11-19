#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
def no_suicide(self,user_input,board):
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
'''

def pat(self,user_input, board):
    if no_suicide(user_input,board) == False:
        return False
    elif no_suicide() == True:
        f = board.damier.values()
        lsp = [] #liste de position de nos pieces alliees
        if self.alternance(board) == 'Noir':
            n = 'N'
        elif self.alternance(board) == 'Blanc':
            n = 'B'
        for j in f:
            if j != None:
                j = str(j)
                if j[2] == "C"+n:
                    lsp.append(int(j[0]),int(j[1]))
                elif j[2] == "R"+n:
                    lsp.append(int(j[0]),int(j[1]))
        lpt = [] #liste de liste de position possible de nos pieces alliees
        for i in lsp:
            lpt.append(board.damier[i].posFuturesPossibles())
        pat = True                                       
        while pat == True:
            for l in lsp:
                for k in lpt[l]:
                    if board.no_suicide((l[0],l[1],k[0],k[2]),board) == True:
                        pat = True
                    else:
                        pat = False
            return True
        return False
                            
       


