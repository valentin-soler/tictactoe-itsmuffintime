import random
import os

# Définir la grille
def creer_grille():
    return [[" " for _ in range(3)] for _ in range(3)]

# Afficher la grille
def afficher_grille(grille):
    os.system("cls" if os.name == "nt" else "clear") #nt pour windows, clear pour linux
    for i, ligne in enumerate(grille):
        print(" | ".join(ligne))
        if i < len(grille) - 1:
            print("-" * 9)

# Vérifier la victoire
def victoire(grille, pos, signe):
    # Cas 1 pos 1 -> [0][0]
    if pos == 1: 
        if grille[0][1] == signe and grille[0][2] == signe:
            return True
        elif grille[1][1] == signe and grille[2][2] == signe:
            return True
        elif grille[1][0] == signe and grille[2][0] == signe:
            return True
        else:
            return False
    # Cas 2 pos 2 -> [0][1]
    elif pos == 2:
        if grille[0][0] == signe and grille[0][2] == signe:
            return True
        elif grille[1][1] == signe and grille[2][1] == signe:
            return True
        else:
            return False
    # Cas 3 pos 3 -> [0][2]
    elif pos == 3:
        if grille[1][2] == signe and grille[2][2] == signe:
            return True
        elif grille[0][0] == signe and grille[0][1] == signe:
            return True
        else:
            return False
    # Cas 4 pos 4 -> [1][0]
    elif pos == 4:
        if grille[0][0] == signe and grille[2][0] == signe:
            return True
        elif grille[1][1] == signe and grille[1][2] == signe:
            return True
        else:
            return False
    # Cas 5 pos 5 -> [1][1]
    elif pos == 5:
        if grille[0][0] == signe and grille[2][2] == signe:
            return True
        elif grille[0][1] == signe and grille[2][1] == signe:
            return True
        elif grille[0][2] == signe and grille[2][0] == signe:
            return True
        elif grille[1][0] == signe and grille[1][2] == signe:
            return True
        else:
            return False
    # Cas 6 pos 6 -> [1][2]
    elif pos == 6:
        if grille[1][0] == signe and grille[1][1] == signe:
            return True
        elif grille[0][2] == signe and grille[2][2] == signe:
            return True
        else:
            return False
    # Cas 7 pos 7 -> [2][0]
    elif pos == 7:
        if grille[1][0] == signe and grille[0][0] == signe:
            return True
        elif grille[1][1] == signe and grille[0][2] == signe:
            return True
        elif grille[2][1] == signe and grille[2][2] == signe:
            return True
        else:
            return False
    # Cas 8 pos 8 -> [2][1]
    elif pos == 8:
        if grille[2][0] == signe and grille[2][2] == signe:
            return True
        elif grille[1][1] == signe and grille[0][1] == signe:
            return True
        else:
            return False
    # Cas 9 pos 9 -> [2][2]
    elif pos == 9:
        if grille[1][1] == signe and grille[0][0] == signe:
            return True
        elif grille[2][1] == signe and grille[2][0] == signe:
            return True
        elif grille[1][2] == signe and grille[0][2] == signe:
            return True
        else:
            return False
    else:
        print("Aucune position connue")
        return False

# Vérifier la présence d'un symbole à une position donnée
def verif_presence(grille, pos):
    i, j = pos_dic[pos]
    return grille[i][j] != " "

# Vérifier le match nul
def nul(grille):
    for ligne in grille:
        if " " in ligne:
            return False
    return True

# IA joue son tour
def ia_jouer(grille):
    # Vérifier si l'IA peut gagner en un coup
    for pos in pos_dic:
        i, j = pos_dic[pos]
        if grille[i][j] == " ":
            grille[i][j] = "O"
            if victoire(grille, int(pos), "O"):
                return int(pos)
            grille[i][j] = " "
    
    # Vérifier si l'adversaire peut gagner en un coup et le bloquer
    for pos in pos_dic:
        i, j = pos_dic[pos]
        if grille[i][j] == " ":
            grille[i][j] = "X"
            if victoire(grille, int(pos), "X"):
                grille[i][j] = "O"
                return int(pos)
            grille[i][j] = " "
    
    # Jouer un coup aléatoire parmi les coups possibles
    coups_possibles = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == " "]
    i, j = random.choice(coups_possibles)
    grille[i][j] = "O"
    return [int(k) for k, v in pos_dic.items() if v == [i, j]][0]

# Gérer le tour du joueur
def joueur_jouer(grille):
    while True:
        pos = input("Entrez une position (1-9): ")
        if pos not in pos_dic:
            print("Position invalide. Essayez encore.")
            continue
        if verif_presence(grille, pos):
            print("Position déjà occupée. Essayez encore.")
            continue
        i, j = pos_dic[pos]
        grille[i][j] = "X"
        return int(pos)

# Dictionnaire des positions
pos_dic = {
    "1": [0, 0],
    "2": [0, 1],
    "3": [0, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "7": [2, 0],
    "8": [2, 1],
    "9": [2, 2]
}

def main():
    grille = creer_grille()
    print("Bienvenue au morpion ! Vous êtes 'X', l'IA est 'O'.")
    afficher_grille(grille)
    
    while True:
        # Tour du joueur
        pos = joueur_jouer(grille)
        afficher_grille(grille)
        if victoire(grille, pos, "X"):
            print("Félicitations, vous avez gagné !")
            break
        if nul(grille):
            print("Match nul !")
            break
        
        # Tour de l'IA
        pos = ia_jouer(grille)
        afficher_grille(grille)
        if victoire(grille, pos, "O"):
            print("L'IA a gagné !")
            break
        if nul(grille):
            print("Match nul !")
            break

if __name__ == "__main__":
    main()