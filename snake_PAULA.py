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
serpent = []
pomme = []
coordonnees_mur = []
coordonnees_serpent =[]

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

 
def creer_premiere_pomme():
    """creation de la premiere pomme du terrain"""
    global pomme
    global POMME
    i=rd.randint(1,18)
    j=rd.randint(1,12)
    if (i,j) in serpent:
        creer_premiere_pomme()
    else:
        pomme.append((i, j))
        POMME=TERRAIN.create_oval(i*30, j*30, (i*30)+30, (j*30)+30, fill = "red")

def fonction_mur():
    """creation des murs qui encadrent le terrain"""
    for i in range(1,19):
        TERRAIN.create_rectangle(i*30,0,(i+1)*30,30,fill='#814436')
        TERRAIN.create_rectangle(i*30,390,(i+1)*30,420,fill='#814436')
        coordonnees_mur.append((i,0))
        coordonnees_mur.append((i,13))
    for j in range(14):
        TERRAIN.create_rectangle(0,j*30,30,(j+1)*30,fill='#814436')
        TERRAIN.create_rectangle(570,j*30,600,(j+1)*30,fill='#814436')
        coordonnees_mur.append((0,j))
        coordonnees_mur.append((19,j))

def creer_pommes():
    """creation de pommes une fois que le serpent a mangé la première"""
    global POMME
    i=rd.randint(1,18)
    j=rd.randint(1,12)
    
    #la pomme ne peut apparaître sur le corps du serpent
    if (i,j) in coordonnees_serpent:
        creer_pommes()
    
    #la pomme ne peut apparaître là où elle a disparu
    elif (i,j) == pomme[0]:
        creer_pommes()

    else:
        del(pomme[0])
        pomme.append((i,j))
        TERRAIN.delete(POMME)
        POMME=TERRAIN.create_oval(i*30, j*30, (i*30)+30, (j*30)+30, fill = "red")

def aggrandir_serpent():
    """le corps du serpent s'aggrandit d'une boule"""
    (i,j)=serpent[0][0]
    
    if direction==0 :
        pass

    elif direction == "haut" :
        serpent.insert(0,[(i,j-1),
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green")])
        coordonnees_serpent.insert(0,(i,j-1))


    elif direction == "bas" :
        serpent.insert(0,[(i,j+1),
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green")])
        coordonnees_serpent.insert(0,(i,j+1))


    elif direction == "droite" :
        serpent.insert(0,[(i+1,j),
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green")])
        coordonnees_serpent.insert(0,(i+1,j))

    elif direction == "gauche" :
        serpent.insert(0,[(i-1,j),
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green")])
        coordonnees_serpent.insert(0,(i-1,j))




#controle direction du serpent
def haut(event):
    """change la direction du serpent"""
    global direction
    if direction != "bas":
        direction = "haut"

def bas(event):
    """change la direction du serpent"""
    global direction
    if direction != "haut":
        direction = "bas"

def droite(event):
    """change la direction du serpent"""
    global direction
    if direction != "gauche":
        direction = "droite"

def gauche(event):
    """change la direction du serpent"""
    global direction
    if direction != "droite":
        direction = "gauche"


#debut du programme
def demarrer():
    """fonction qui commence le jeu avec un serpent au milieu"""   
    global serpent
    global coordonnees_serpent
    serpent.extend(
    [[(10,7),TERRAIN.create_oval(300, 210, 330, 240, fill = "green")],
    [(10,7),TERRAIN.create_oval(300, 210, 330, 240, fill = "green")],
    [(10,7),TERRAIN.create_oval(300, 210, 330, 240, fill = "green")]]
    )  
    coordonnees_serpent=[(10,7),(10,7),(10,7)]
    mouvement()
    

def etape_mouvement(i,j):
    if direction == 0 :
        pass

    elif direction == "haut" :
        #TERRAIN.move(serpent[-1][1], 0, -30)
        serpent.append([(i,j-1),
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green")])

        TERRAIN.delete(serpent[0][1])
        del serpent[0]
        coordonnees_serpent.append((i,j-1))
        del coordonnees_serpent[0]


    elif direction == "bas" :
        #TERRAIN.move(serpent[-1][1], 0, 30)
        serpent.append([(i,j+1),
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green")])

        TERRAIN.delete(serpent[0][1])
        del serpent[0]
        coordonnees_serpent.append((i,j+1))
        del coordonnees_serpent[0]


    elif direction == "droite" :
        #TERRAIN.move(serpent[-1][1], 30, 0)
        serpent.append([(i+1,j),
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green")])

        TERRAIN.delete(serpent[0][1])
        del serpent[0]
        coordonnees_serpent.append((i+1,j))
        del coordonnees_serpent[0]


    elif direction == "gauche" :
        #TERRAIN.move(serpent[-1][1], -30, 0)
        serpent.append([(i-1,j),
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green")])
        
        TERRAIN.delete(serpent[0][1])
        del serpent[0]
        coordonnees_serpent.append((i-1,j))
        del coordonnees_serpent[0]


def mouvement():
    """fonction qui fait bouger le serpent"""
    global id_after
    (i,j) = serpent[-1][0]
    etape_mouvement(i,j) 

    #le serpent s'arrête lorsqu'il touche le mur
    if serpent[-1][0] in coordonnees_mur:
        id_after=TERRAIN.after(1,None)
    
    #le serpent s'aggrandit quand il touche une pomme
    elif serpent[-2][0] in pomme:
        aggrandir_serpent()
        creer_pommes()
        id_after = TERRAIN.after(300,mouvement)

    #if case de devant est vide
    else:
        id_after = TERRAIN.after(300, mouvement)
    

    
    



#########################################
# programme principal

racine = tk.Tk()

TERRAIN = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR, bg = "grey20")
TERRAIN.grid()

quadrillage()
demarrer()
creer_premiere_pomme()
fonction_mur()

#########################################
# définition des widgets


#########################################
# définition des évènements

racine.bind("<KeyPress-Up>", haut)
racine.bind("<KeyPress-Down>", bas)
racine.bind("<KeyPress-Right>", droite)
racine.bind("<KeyPress-Left>", gauche)

tk.mainloop()