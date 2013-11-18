#! c:/Python33 python
# -*- coding:Utf8 -*-


'''
Created on Nov 17, 2013

@author: Simon
'''

from chess.plateau import Plateau

board = Plateau()
#print(board.damier)
#print(board.damier[1,1])
#print(board.damier[1,1].abouge)
#print('\u2656')

'''import os
cwd = os.getcwd()
path = os.path.join(cwd, "my_file")
print(path)'''

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
    print(path)

    f = open(path, "r")
    lines = f.readlines()
    for i in lines:
        pieces = {'T':Tour, 'C':Cavalier, 'F':Fou, 'D':Dame, 'R':Roi, 'P':Pion}
        print(i)
        #print(board.damier[(i[0],i[1])])
        #board.damier[(i[0],i[1])] = pieces[i[2]](i[0],i[1],i[3])
    f.close()
    print(board.damier)
    return board

load_game("tests_prof\jeu1")