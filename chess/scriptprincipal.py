'''
Created on Nov 4, 2013

@author: Simon
'''

if __name__ == '__main__':
    pass

### Menu principal( jeu par création, jeu par chargement)
### Menu ( jouer le tour, arrêter et sauvegarder)
### affichage à chaque tour



board = []
for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)
