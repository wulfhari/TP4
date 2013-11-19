#! c:/Python33 python
# -*- coding:Utf8 -*-

def transformation(board):
    
    from chess.dame import Dame    
    from chess.pion import Pion
     
    for i in range(0,8):
        if board[0,i] == Pion:
            board[0,i] = Dame(0,i,board[0,i].color)
    for i in range(0,8):
        if board[7,i] == Pion:
            board[7,i] = Dame(7,i,board[0,i].color)
        
       