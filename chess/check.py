

def echec(self):
    from plateau import Plateau
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
    
    #Quelle roi doit-on cherche?
    if active_player == "Noir":
        n = N
        m = B
    elif active_player == "Blanc":
        n = B
        m = N
    
    #Pour recuperer l'emplacement du roi sur le damier
    for i in f:
        if i[2:] == "R"+n:
            posR = (i[0],i[1])
        else:
            pass
    #Pour recuperer en liste l'emplacement des pieces 'roi et/ou cavalier' de couleur adverse sur le damier
    for j in f:
        if j[2] == "C"+m:
            lsp.append = (j[0],j[1])
        elif j[2] == "R"+m:
            lsp.append = (j[0],j[1])

    #Pour recuperer en liste l'emplacement des pieces 'pion,tour,dame et fou' de couleur adverse sur le damier
    for k in f:
        if k[2] == "P"+m:
            pk.append = (k[0],k[1])
        elif k[2] == "T"+m:
            pk.append = (k[0],k[1])
        elif k[2] == "D"+m:
            pk.append = (k[0],k[1])
        elif k[2] == "F"+m:
            pk.append = (k[0],k[1])

    #Pour chaque roi ou cavalier adverse est-ce que le roi est dans leur liste de position possibles
    for l in lsp:
        if posR in posFuturesPossibles(lsp[l],plateau):
            return True

    #Pour chaque pion, tour, dame ou fou adverse est-ce que le roi est dans un de leur déplacement valide
    for h in pk:
        elif deplacementValide(pk[h],posR,plateau) == True:
            return True
    else:
        return False