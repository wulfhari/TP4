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


file_name = "save.txt"
import os
cwd = os.getcwd()
path = os.path.join(cwd, file_name)        
f = open(path, "w")
#for key in board:
#   if board[key][2] == T:
for key in board.damier:
    if board.damier[(key)] != None:
        f.write(str((board.damier[(key)])))
#f.write(str(board.tour,+tour.abouge, +tour.abouge, +tour.abouge )+"\n")
f.close()