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
buffer = 0
score = 0
vitesse_serpent = 600
murs = []
serpent = []
pomme = []
coordonnees_mur = []
coordonnees_serpent =[]

#########################################
# définition des fonctions


#fonction quadrillage qui doit disparaitre
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

 
#################################################################################
# debut du snake- pomme - murs - serpent#
#################################################################################

def creer_premiere_pomme():
    """creation de la premiere pomme du terrain"""
    global pomme
    global POMME

    i=rd.randint(1,18)
    j=rd.randint(1,12)
    
    #la pomme ne peut pas apparaitre dans le serpent
    if (i,j) in coordonnees_serpent :
        creer_premiere_pomme()
    
    else:
        pomme.append((i, j))
        POMME=TERRAIN.create_oval(i*30, j*30, (i*30)+30, (j*30)+30, fill = "red")


def fonction_mur():
    """creation des murs qui encadrent le terrain"""
    global murs
    for i in range(1,19):
        murs.append(TERRAIN.create_rectangle(i*30,0,(i+1)*30,30,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(i*30,390,(i+1)*30,420,fill='#814436'))
        coordonnees_mur.append((i,0))
        coordonnees_mur.append((i,13))
    for j in range(14):
        murs.append(TERRAIN.create_rectangle(0,j*30,30,(j+1)*30,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(570,j*30,600,(j+1)*30,fill='#814436'))
        coordonnees_mur.append((0,j))
        coordonnees_mur.append((19,j))


def demarrer():
    """fonction qui commence le jeu avec un serpent au milieu"""   
    global serpent
    global coordonnees_serpent

    serpent.extend(
    [TERRAIN.create_oval(300, 210, 330, 240, fill = "green"),
    TERRAIN.create_oval(300, 210, 330, 240, fill = "green"),
    TERRAIN.create_oval(300, 210, 330, 240, fill = "green")]
    )  
    coordonnees_serpent=[(10,7),(10,7),(10,7)]
    mouvement()


#################################################################################
# mouvement du serpent - boucle after
#################################################################################


#controle direction du serpent
def haut(event):
    """change la direction du serpent"""
    global buffer
    if direction != "bas":
        buffer = "haut"

def bas(event):
    """change la direction du serpent"""
    global buffer
    if direction != "haut":
        buffer = "bas"

def droite(event):
    """change la direction du serpent"""
    global buffer
    if direction != "gauche":
        buffer = "droite"

def gauche(event):
    """change la direction du serpent"""
    global buffer
    if direction != "droite":
        buffer = "gauche"



def etape_mouvement(i,j):
    """fonction qui fait bouger le serpent d une case dans la direction indiquée"""
    global direction

    if buffer == 0 :
        pass

    elif buffer == "haut" :
        serpent.append(
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))

        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i,j-1))
        del coordonnees_serpent[0]
        
        direction = "haut"

    elif buffer == "bas" :
        serpent.append(
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))

        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i,j+1))
        del coordonnees_serpent[0]
        direction = "bas"


    elif buffer == "droite" :
        serpent.append(
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))

        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i+1,j))
        del coordonnees_serpent[0]
        
        direction = "droite"


    elif buffer == "gauche" :
        serpent.append(
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))
        
        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i-1,j))
        del coordonnees_serpent[0]

        direction = "gauche"


def mouvement():
    """fonction qui fait bouger le serpent et fait le test en cas de victoire/defaite"""
    global id_after
    (i,j) = coordonnees_serpent[-1]
    etape_mouvement(i,j) 

    #le serpent s'arrête lorsqu'il touche le mur
    if coordonnees_serpent[-1] in coordonnees_mur:
        game_over()
    
    #le serpent s'aggrandit quand il touche une pomme
    elif coordonnees_serpent[-2] in pomme:
        aggrandir_serpent()
        augmenter_score()
        creer_pommes()
        id_after = TERRAIN.after(300,mouvement)

    #if case de devant est vide
    else:
        id_after = TERRAIN.after(300, mouvement)


#################################################################################
# snake mange une pomme - creer nouvelle pomme - agrandir snake - augmenter score
#################################################################################

def augmenter_score():
    """augmente le score et change le texte indiquant le score"""
    global label_score
    global score

    score += 1
    print(score)
    label_score.config(text= "score : " + str(score))
    

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
    (i,j)=coordonnees_serpent[0]
    
    if direction==0 :
        pass

    elif direction == "haut" :
        serpent.insert(0,
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))
        coordonnees_serpent.insert(0,(i,j-1))


    elif direction == "bas" :
        serpent.insert(0,
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))
        coordonnees_serpent.insert(0,(i,j+1))


    elif direction == "droite" :
        serpent.insert(0,
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))
        coordonnees_serpent.insert(0,(i+1,j))

    elif direction == "gauche" :
        serpent.insert(0,
        TERRAIN.create_oval(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))
        coordonnees_serpent.insert(0,(i-1,j))


#################################################################################
# snake prends un mur - game over
#################################################################################
""" attention fonction pas finies"""
def game_over():
    global id_after
    global id_text
    global score
    
    TERRAIN.after_cancel(id_after)
    id_text = []
    id_text.extend([TERRAIN.create_rectangle((180,175),(420,225), fill = "black"),
                    TERRAIN.create_text(300,200, text = "GAME OVER", fill = "red", font = ("Helvetica", 32))])
    
    score = 0
    TERRAIN.after(1000, lambda : transition_vers_menu())


def transition_vers_menu():
    global id_text
    global serpent, coordonnees_serpent, coordonnees_mur, murs, buffer
    buffer = 0
    coordonnees_serpent = []
    for i in serpent:
        TERRAIN.delete(i)
    serpent= []
    for i in murs :
        TERRAIN.delete(i)
    murs = []
    TERRAIN.delete(id_text[0])
    TERRAIN.delete(id_text[1])



#################################################################################
#################################################################################
# fonctions du menu 
#################################################################################
#################################################################################

def valider(event):
    global vitesse_serpent
    vitesse_serpent=demande_vitesse.get()
    demande_vitesse.delete(0,6)

def vitesse1():
    global vitesse_serpent
    vitesse_serpent=900

def vitesse2():
    global vitesse_serpent
    vitesse_serpent=600

def vitesse3():
    global vitesse_serpent
    vitesse_serpent=300


#################################################################################
# fenetre des regles du jeu
#################################################################################
def comment_jouer():
    fenetre = tk.Toplevel(root)
    fenetre.title("Les débuts")


#################################################################################
# fenetre du tableau des scores
#################################################################################
def scores():
    f = tk.Toplevel(root)
    f.title("Tableau des scores")
 


#################################################################################
# fenetre snake
#################################################################################
def commencer():
    """fonction qui ouvre le jeu snake dans une fenetre a part"""
    global TERRAIN
    global label_score

    #creation de la fenetre
    fenetre = tk.Toplevel(root)
    fenetre.title("SNAKE")

    #creation des widgets
    label_score= tk.Label(fenetre, text = "score : 0")
    label_score.grid(row = 0)
    TERRAIN = tk.Canvas(fenetre, height = HAUTEUR, width = LARGEUR, bg = "grey20")
    TERRAIN.grid(row = 1)

    fenetre.bind("<KeyPress-Up>", haut)
    fenetre.bind("<KeyPress-Down>", bas)
    fenetre.bind("<KeyPress-Right>", droite)
    fenetre.bind("<KeyPress-Left>", gauche)
   
    #programme principal
    quadrillage()
    demarrer()
    creer_premiere_pomme()
    fonction_mur()


#################################################################################
#################################################################################
# creation du menu
#################################################################################
#################################################################################


#################################################################################
# création de la fenêtre et des widgets
#################################################################################
root = tk.Tk()
root.geometry("800x650")
root.title("Création du menu")


canvas = tk.Canvas(root, bg="dark green", height=650, width=800)
canvas.grid(rowspan = 8, columnspan = 6)

  

titre = tk.Label(root, text="SNAKE", font=("Helvetica", "28"), bg="dark green", fg="white")
niveaux = tk.Label(root, text="LEVELS", font=("Helvetica", "16"), bg="dark green", fg="white")

niveau_1 = tk.Radiobutton(root, text="Level 1 : Easy", 
                        font=("Helvetica", "16"), bg="dark green", fg="white", 
                        indicatoron=1, relief="raised")
niveau_2 = tk.Radiobutton(root, text="Level 2 : Medium",
                        font=("Helvetica", "16"), bg="dark green", fg="white",
                        indicatoron=1, relief="raised")
niveau_3 = tk.Radiobutton(root, text="Level 3 : Hard",
                        font=("Helvetica", "16"), bg="dark green", fg="white",
                        indicatoron=1, relief="raised")

vitesse = tk.Label(root, text="SPEED", font=("Helvetica", "16"), bg="dark green", fg="white")

vitesse_1 = tk.Radiobutton(root, text="Slow",
                        font=("Helvetica", "16"), bg="dark green", fg="white",
                        indicatoron=1, relief="raised")
vitesse_2 = tk.Radiobutton(root, text="Normal",
                        font=("Helvetica", "16"), bg="dark green", fg="white",
                        indicatoron=1, relief="raised")
vitesse_3 = tk.Radiobutton(root, text="Fast",
                        font=("Helvetica", "16"), bg="dark green", fg="white",
                        indicatoron=1, relief="raised")

vitesse_personalisee = tk.Label(root, text="CHOOSE YOUR SPEED", font=("Helvetica", "16"), bg="dark green", fg="white")
Label1=tk.Label(root,text='mvt/ms',font=('Helvetica',10),bg='darkgreen',fg='white')
Label2=tk.Label(root,text='PRESS ENTER TO CONFIRM',font=('Helvetica',10),bg='darkgreen',fg='white')

demande_vitesse=tk.Entry(root,bg='darkgreen',fg='white')



#################################################################################
# placement des widgets
#################################################################################

titre.grid(column=0, row=0, columnspan=3)
niveaux.grid(column=0, row=1, columnspan=3)
niveau_1.grid(column=0, row=2)
niveau_2.grid(column=1, row=2)
niveau_3.grid(column=2, row=2)
vitesse.grid(column=0, row=3, columnspan=3)
vitesse_1.grid(column=0, row=4)
vitesse_2.grid(column=1, row=4)
vitesse_3.grid(column=2, row=4)
vitesse_personalisee.grid(column=0, row=5, columnspan=3)
Label1.grid(column=1,row=6,sticky='es')
Label2.grid(column=1,row=7,sticky='n')
demande_vitesse.grid(column=1,row=6, sticky='s')


#################################################################################
# widgets du menu deroulant
#################################################################################

mainmenu = tk.Menu(root)

regles = tk.Menu(mainmenu, tearoff=0)
regles.add_command(label="Comment jouer", command=comment_jouer)
regles.add_separator()
regles.add_command(label="Quitter", command=root.quit)

tab = tk.Menu(mainmenu, tearoff=0)
tab.add_command(label="Tableau des scores", command=scores)
tab.add_separator()
tab.add_command(label="Quitter", command=root.quit)

debut = tk.Menu(mainmenu, tearoff=0)
debut.add_command(label="Commencer", command=commencer)

mainmenu.add_cascade(label="Règles du jeu", menu=regles)
mainmenu.add_cascade(label="Tableau des scores", menu=tab)
mainmenu.add_cascade(label="Commencer", menu=debut)


#################################################################################
# gestion des evenements
#################################################################################
root.bind("<KeyPress-Up>", haut)
root.bind("<KeyPress-Down>", bas)
root.bind("<KeyPress-Right>", droite)
root.bind("<KeyPress-Left>", gauche)
root.bind('<KeyPress-Return>',valider)


# boucle principale

root.config(menu=mainmenu)
root.mainloop()