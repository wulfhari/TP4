# -*- coding:Utf-8 -*-

def affichage_plateau():
    from chess.plateau import Plateau
    board = Plateau()
    list=[]
        
        
    caracteres_unicode_pieces = {'TB': '\u2656',
                                     'CB': '\u2658',
                                     'FB': '\u2657',
                                     'KB': '\u2654',
                                     'QB': '\u2655',
                                     'PB': '\u2659',
                                     'TN': '\u265C',
                                     'CN': '\u265E',
                                     'FN': '\u265D',
                                     'KN': '\u265A',
                                     'QN': '\u265B',
                                     'PN': '\u265F',}
    for x in range(0,8):
        list.append(["0"]*8)
            
    for i in range(0,8):
        for j in range(0,8):
           # if board.damier[i][j] != None:
            list[i][j]=board.damier[(i,j)]
            if 'TN' in str(list[i][j]):
                list[i][j]=caracteres_unicode_pieces['TN']
            
    for y in range(0,8):
        print(list[y])
    #print(list)
    #print(str(list[0][0]))
    print(c for c,v in board.damier.items() if v=="00TN")
    
affichage_plateau()
               
