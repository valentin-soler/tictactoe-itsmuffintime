#Definir limite de la grille
def creer_board():
    return [[" " for _ in range(3)] for _ in range(3)]

#Définir symbole de la grille
def afficher_board(grille):
    for i, ligne in enumerate(board):
        print(" | ".join(ligne))
        if i < len(grille) - 1: 
            print("-" * 9)

# Création de la grille
board = creer_board()

# Affichage de la grille
print("Bienvenue au morpion ! Vous êtes 'X', l'IA est 'O'.")
afficher_board(board)



