pos_dic = {
    "1": [0,0],
    "2": [0,1],
    "3": [0,2],
    "4": [1,0],
    "5": [1,1],
    "6": [1,2],
    "7": [2,0],
    "8": [2,1],
    "9": [2,2]
}

def verif_presence(grille,pos):
    if "x" or "o" in grille[pos_dic.get(pos)[0]][pos_dic.get(pos)[0]]:
        return True
    else :
        return False