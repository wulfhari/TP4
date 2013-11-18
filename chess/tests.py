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

for key in board.damier:
    print(board.damier[key][0]+board.damier[key][1]+board.damier[key][2]+board.damier[key][3])