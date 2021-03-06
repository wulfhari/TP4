#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on Nov 4, 2013

@author: Simon
'''

class GameManagement(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def save_game(self, board, file_name):
        file_name = file_name+".txt"
        import os
        cwd = os.getcwd()
        path = os.path.join(cwd, file_name)        
        f = open(path, "w")
        Line1_list = [board.tour, board.damier[(0,0)].abouge, board.damier[(0,7)].abouge, board.damier[(7,0)].abouge, board.damier[(7,7)].abouge]
        for i in Line1_list:
            f.write(str(i)+" ")
        f.write("\n") 
               
        for key in board.damier:
            if board.damier[(key)] != None:
                f.write(str((board.damier[(key)]))+"\n")    
        f.close()

            
    def load_game(self, file_name):
        
        from chess.plateau import Plateau
        from chess.tour import Tour
        from chess.dame import Dame
        from chess.roi import Roi
        from chess.pion import Pion
        from chess.fou import Fou
        from chess.cavalier import Cavalier
        
        board = Plateau()
        board.damier = {}
        
        file_name = file_name+".txt"
        import os
        cwd = os.getcwd()
        path = os.path.join(cwd, file_name)
            
        f = open(path, "r")
        lines = f.readlines()
        first_line = lines[0]
        pieces = {'T':Tour, 'C':Cavalier, 'F':Fou, 'D':Dame, 'R':Roi, 'P':Pion}
        couleur = {'B':1,'N':0}
        
        board.tour = int(first_line[0])
        
        for i in range(1,len(lines)):
            line = lines[i]
            board.damier[(int(line[0]),int(line[1]))] = pieces[line[2]](int(line[0]),int(line[1]),couleur[line[3]])
            
        if board.damier[(7,7)] != None:    
            board.damier[(7,7)].abouge = int(first_line[2])
        elif board.damier[(7,0)] != None:    
            board.damier[(7,0)].abouge = int(first_line[4])
        elif board.damier[(0,7)] != None:
            board.damier[(0,7)].abouge = int(first_line[6])
        elif board.damier[(0,0)] != None:
            board.damier[(0,0)].abouge = int(first_line[8])

        
        f.close()
       
        return board
       
    def new_game(self):
        from chess.plateau import Plateau
        board = Plateau()
        return board
        
    
### Alternance des joueurs        
    def alternance(self, board):
        
        if float(board.tour)%2 == 0:
            active_player = 'Blanc'
        else:
            active_player = 'Noir'
        return active_player        
        '''        
        if active_player == "Noir":
            active_player = "Blanc"
        elif active_player == "Blanc":
            active_player = "Noir"
        return active_player
        '''
    
    def next_turn(self, user_input, board):
        
        
        #if GameManagement.echecEtMat != True:
        
        board.damier[(int(user_input[0]),int(user_input[1]))].deplacer((int(user_input[2]),int(user_input[3])), board)
        #self.transformation(board)
        
           
        
### Coups Speciaux, Echec, echec et mat, pat, ROC        
        
    def transformation(self,board):
        '''
        from chess.dame import Dame    
        from chess.pion import Pion
         
        for i in range(0,8):
            if board[(0,i)] == Pion:
                board[(0,i)] = Dame(0,i,board[(0,i)].color)
        for i in range(0,8):
            if board[(7,i)] == Pion:
                board[(7,i)] = Dame(7,i,board[(0,i)].color)
        '''
    
    def echec(self, board):
        f = board.damier.values()
        lsp = []
        pk = []
        
        self.alternance(board)#Quelle roi doit-on cherche?
        if self.alternance(board) == 'Noir':
            n = 'N'
            m = 'B'
        elif self.alternance(board) == 'Blanc':
            n = 'B'
            m = 'N'
        
        #Pour recuperer l'emplacement du roi sur le damier
        for i in f:
            if i != None:
                i = str(i)
                if i[2:] == "R"+n:
                    posR = [int(i[0]),int(i[1])]
                else:
                    pass
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
    
    def echecEtMat(self,board):
        if board.echec() == True:
            f = board.damier.values()
            self.alternance(board)#Quelle roi doit-on cherche?
            if self.alternance(board) == 'Noir':
                n = 'N'
                m = 'B'
            elif self.alternance(board) == 'Blanc':
                n = 'B'
                m = 'N'
             #Pour recuperer l'emplacement du roi sur le damier
            for i in f:
                if i != None:
                    i = str(i)
                    if i[2:] == "R"+n:
                        posR = [int(i[0]),int(i[1])]
                    else:
                        pass
            if board.damier[posR].posFuturesPossibles() == 0:
                    pat() 
            else:
                return False
            
        elif boar.echec()== False:
            return False
    
    
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
                        else:
                            pass
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
                        else:
                            pass  
                #Pour chaque roi ou cavalier adverse est-ce que le roi est dans leur liste de position possibles
                for l in lsp:
                    if posR in board.damier[l].posFuturesPossibles():
                        return True   
                #Pour chaque pion, tour, dame ou fou adverse est-ce que le roi est dans un de leur deplacement valide
                for h in pk:
                    if board.damier[h].deplacementValide(posR, board) == True:
                        return True 
            #Pour quand une piece autre que roi est deplacee    
            else:
                board_2 = board.damier
                board.damier[(int(user_input[0]),int(user_input[1]))].deplacer((int(user_input[2]),int(user_input[3])), board_2)
                board_2.echec(board_2)

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
            
    
    def ROC(self):
        pass
    
    def en_passant(self):
        pass        
