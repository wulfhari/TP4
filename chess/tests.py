#! c:/Python33 python
# -*- coding:Utf8 -*-

def load_game(file_name):
    
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
    
    board.tour = first_line[0]
    
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
    print(board.damier)
    return board

load_game("tests_prof\jeuF")
