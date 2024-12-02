#Definir limite de la grille
def creer_grille():
    return [[" " for _ in range(3)] for _ in range(3)]

#Définir symbole de la grille
def afficher_grille(grille):
    for i, ligne in enumerate(grille):
        print(" | ".join(ligne))
        if i < len(grille) - 1: 
            print("-" * 9)

# Création de la grille
grille = creer_grille()

# Affichage de la grille
print("Bienvenue au morpion ! Vous êtes 'X', l'IA est 'O'.")
afficher_grille(grille)

