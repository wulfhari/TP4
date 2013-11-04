'''
Created on Nov 4, 2013

@author: Simon
'''

if __name__ == '__main__':
    pass

board = []
for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)
