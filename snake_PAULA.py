#########################################
# groupe LDDMP 3
# Ismaël RAIS
# Ines ROSENTHAL
# Hajar ASBAI
# Adrien HANNA
# Quentin ASSIE
# Paula POP
# https://github.com/uvsq22001770/Projet_2.git
#########################################

# import des librairies

import tkinter as tk
import random as rd 


#########################################
# définition des constantes

coté = 30
LARGEUR = 600
HAUTEUR = 420
COULEUR_QUADR = "grey60"

#########################################
# définition des variables globales
direction = 0
serpent = 0
pomme = []
#########################################
# définition des fonctions
# docstring pour chaque fonction

def quadrillage():
    """ATTENTION le quadrillage doit disparaitre pour le rendu final"""
    y = 0
    while y <= HAUTEUR:
        TERRAIN.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += coté
    x = 0
    while x <= LARGEUR:
        TERRAIN.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        x += coté


def creer_pomme():
    global pomme
    i=rd.randint(0, 19) 
    j=rd.randint(0, 14)
    pomme.append((i, j))
    pomme.append(TERRAIN.create_oval(i*30, j*30, (i*30)+30, (j*30)+30, fill = "red"))
    return pomme


#controle direction du sepent
def haut(event):
    """change la direction du serpent"""
    global direction
    direction = "haut"

def bas(event):
    """change la direction du serpent"""
    global direction
    direction = "bas"

def droite(event):
    """change la direction du serpent"""
    global direction
    direction = "droite"

def gauche(event):
    """change la direction du serpent"""
    global direction
    direction = "gauche"


#debut du programme
def demarrer():
    """fonction qui commence le jeu avec un serpent au milieu"""   
    global serpent
    serpent = TERRAIN.create_oval(300, 210, 330, 240, fill = "green")  
    mouvement()

def mouvement():
    """fonction qui fait bouger le serpent"""
    if direction == 0 :
        pass
    elif direction == "haut" :
        TERRAIN.move(serpent, 0, -30)
    elif direction == "bas" :
        TERRAIN.move(serpent, 0, 30)
    elif direction == "droite" :
        TERRAIN.move(serpent, 30, 0)
    elif direction == "gauche" :
        TERRAIN.move(serpent, -30, 0)

    id_after = TERRAIN.after(750, mouvement)   


#########################################
# programme principal

racine = tk.Tk()

TERRAIN = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR, bg = "grey20")
TERRAIN.grid()

quadrillage()
demarrer()
creer_pomme()

#########################################
# définition des widgets


#########################################
# définition des évènements

racine.bind("<KeyPress-Up>", haut)
racine.bind("<KeyPress-Down>", bas)
racine.bind("<KeyPress-Right>", droite)
racine.bind("<KeyPress-Left>", gauche)

tk.mainloop()