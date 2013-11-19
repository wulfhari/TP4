

def echec(self, board):
    from chess.plateau import Plateau
    from chess.tour import Tour
    from chess.dame import Dame
    from chess.roi import Roi
    from chess.pion import Pion
    from chess.fou import Fou
    from chess.cavalier import Cavalier
    
    f = board.damier.values()
    lsp = []
    pk = []
    
    self.alternance(board)#Quelle roi doit-on cherche?
    if self.alternance(board) == 'Noir':
        n = 'N'
        m = 'B'
    elif self.alternance(board) == 'Blanc':
        n = 'B'
        m = 'N'
    
    #Pour recuperer l'emplacement du roi sur le damier
    for i in f:
        if i != None:
            i = str(i)
            if i[2:] == "R"+n:
                posR = [int(i[0]),int(i[1])]
            else:
                pass
    #Pour recuperer en liste l'emplacement des pieces 'roi et/ou cavalier' de couleur adverse sur le damier
    for j in f:
        if j != None:
            j = str(j)
            if j[2] == "C"+m:
                lsp.append(int(j[0]),int(j[1]))
            elif j[2] == "R"+m:
                lsp.append(int(j[0]),int(j[1]))

    #Pour recuperer en liste l'emplacement des pieces 'pion,tour,dame et fou' de couleur adverse sur le damier
    for k in f:
        if k != None:
            k = str(k)
            if k[2] == "P"+m:
                pk.append(int(k[0]),int(k[1]))
            elif k[2] == "T"+m:
                pk.append(int(k[0]),int(k[1]))
            elif k[2] == "D"+m:
                pk.append(int(k[0]),int(k[1]))
            elif k[2] == "F"+m:
                pk.append(int(k[0]),int(k[1]))

    #Pour chaque roi ou cavalier adverse est-ce que le roi est dans leur liste de position possibles
    for l in lsp:
        if posR in board.damier[l].posFuturesPossibles():
            return True


    #Pour chaque pion, tour, dame ou fou adverse est-ce que le roi est dans un de leur deplacement valide
    for h in pk:
        if board.damier[h].deplacementValide(posR, board) == True:
            return True
    
    else:
        return False