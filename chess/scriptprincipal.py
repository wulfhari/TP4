'''
Created on Nov 4, 2013

@author: Simon
'''

if __name__ == '__main__':
    pass

### Menu principal( jeu par cr�ation, jeu par chargement)
### Menu ( jouer le tour, arr�ter et sauvegarder)
### affichage � chaque tour



board = []
for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)
