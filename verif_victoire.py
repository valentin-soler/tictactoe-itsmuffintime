def nul(grille):
    if " " in grille:
        return False
    return True

def victoire(grille,pos,signe): #Pos --> Position du coup joué # signe --> X ou O
    #Cas 1 pos 1 -> [0][0]
    if pos == 1: 
        if grille[0][1] == signe and grille[0][2] == signe:
            return True
        elif grille[1][1] == signe and grille[2][2] == signe:
            return True
        elif grille[1][0] == signe and grille[1][0] == signe:
            return True
        else :
            return False
    #Cas 2 pos 2 -> [0][1]