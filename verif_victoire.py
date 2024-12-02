#Nul --> retourn True s'il y a match nul et False s'ils peuvent encore joués
def nul(grille):
    if " " in grille:
        return False
    return True

#Victoire --> Retourne True si le joueur a gagné et False s'il a perdu
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
    elif pos == 2:
        if grille[0][0] == signe and grille[0][2] == signe:
            return True
        elif grille[1][1] == signe and grille[2][1] == signe:
            return True
        else :
            return False
    #Cas 3 pos 3 -> [0][2]
    elif pos == 3:
        if grille[1][2] == signe and grille[2][2] == signe:
            return True
        elif grille[0][0] == signe and grille[0][1] == signe:
            return True
        else :
            return False
    #Cas 4 pos 4 -> [1][0]
    elif pos == 4:
        if grille[0][0] == signe and grille[2][0] == signe:
            return True
        elif grille[1][1] == signe and grille[1][2] == signe:
            return True
        else:
            return False
    #Cas 5 pos 5 -> [1][1]
    elif pos == 5:
        if grille[0][0] == signe and grille[2][2] == signe:
            return True
        elif grille[0][1] == signe and grille[2][1] == signe:
            return True
        elif grille[0][2] == signe and grille[2][0] == signe:
            return True
        elif grille[1][0] == signe and grille[1][2] == signe:
            return True
        else :
            return False
    # Cas 6 pos 6 -> [1][2]
    elif pos == 6:
        if grille[1][0] == signe and grille[1][1]:
            return True
        elif grille[0][2] == signe and grille[2][2]:
            return True
        else:
            return False
    #Cas 7 pos 7 -> [2][0]
    elif pos == 7:
        if grille[1][0] == signe and grille[0][0] == signe:
            return True
        elif grille[1][1] == signe and grille[0][2] == signe:
            return True
        elif grille[2][1] == signe and grille[2][2] == signe:
            return True
        else:
            return False
    #Cas 8 pos 8 -> [2][1]
    elif pos == 8:
        if grille[2][0] == signe and grille[2][2] == signe:
            return True
        elif grille[1][1] == signe and grille[0][1] == signe:
            return True
        else:
            return False
    #Cas 9 pos 9 -> [2][2]
    elif pos == 9:
        if grille[1][1] == signe and grille[0][0] == signe:
            return True
        elif grille[2][1] == signe and grille[2][0] == signe:
            return True
        elif grille[1][2] == signe and grille[0][2] == signe:
            return True
        else:
            return False
    else :
        print("Aucune position connu")