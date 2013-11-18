# -*- coding:Utf-8 -*-

def affiche_plateau(board):
           
    unicode_dict =  {'TB': '\u2656',
                     'CB': '\u2658',
                     'FB': '\u2657',
                     'RB': '\u2654',
                     'DB': '\u2655',
                     'PB': '\u2659',
                     'TN': '\u265C',
                     'CN': '\u265E',
                     'FN': '\u265D',
                     'RN': '\u265A',
                     'DN': '\u265B',
                     'PN': '\u265F',}
    
    liste1 = board.damier.values()
    uni_list = []
    
    #Affiche un quadrillage de 0 8*8
    for x in range(0,8):
        uni_list.append(["0"]*8)  
    
    for i in liste1:
        if i != None:
            i = str(i)
            if i[2:] in unicode_dict:
                unic = unicode_dict[i[2:]]
                uni_list[int(i[0])][int(i[1])] = unic
                
        
    for row in uni_list:
        print(" ".join(row))
                

from chess.plateau import Plateau

board = Plateau()

affiche_plateau(board)


