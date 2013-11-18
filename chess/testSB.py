# -*- coding:Utf-8 -*-

def affichage_plateau():
    from chess.plateau import Plateau
    from chess.tour import Tour
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
    liste1 = board.damier.values()
    for i in liste1:
        if i[2:] == 'TN':
            i == '\u265C'
    print(liste1)
    print(str(board.damier.values()))
                
                
          #  if 'TN' in list[i][j]:
               # list[i][j]=caracteres_unicode_pieces['TN']
            
    #for y in range(0,8):
      #  print(list[y])

    
affichage_plateau()

               
