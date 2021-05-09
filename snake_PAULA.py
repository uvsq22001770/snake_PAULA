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
variable_mur = 1
vitesse_serpent = 600
murs = []
serpent = []
pomme = []
coordonnees_mur = []
coordonnees_serpent = []
pseudos_joueur = []
L = []

liste_username_score=[ ["Username", 0], ["Username", 0],
   ["Username", 0], ["Username", 0], ["Username", 0], ["Username", 0],
   ["Username", 0], ["Username", 0], ["Username", 0] ]

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
    global coordonnees_mur

    pomme = []
    POMME = []

    i=rd.randint(1,18)
    j=rd.randint(1,12)
    
    #la pomme ne peut pas apparaitre dans le serpent
    if (i,j) in coordonnees_serpent :
        creer_premiere_pomme()
    
    #la pomme ne peut pas apparaître sur un mur interne
    if (i,j) in coordonnees_mur :
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

def murs_2():
    global murs
    global TERRAIN
    for i in range(5,13):
        murs.append(TERRAIN.create_rectangle(i*30,3*30,(i+1)*30,30*3+30,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(i*30,390,(i+1)*30,420,fill='#814436'))
        coordonnees_mur.append((i,3))
        coordonnees_mur.append((i,13))
    for j in range(4,6):
        murs.append(TERRAIN.create_rectangle(5*30,j*30,30+5*30,(j+1)*30,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(570,j*30,600,(j+1)*30,fill='#814436'))
        coordonnees_mur.append((5,j))
        coordonnees_mur.append((19,j))

def murs_3():
    global TERRAIN
    global murs
    for i in range(12,16):
        murs.append(TERRAIN.create_rectangle(i*30,7*30,(i+1)*30,30+7*30,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(i*30,390,(i+1)*30,420,fill='#814436'))
        coordonnees_mur.append((i,7))
        coordonnees_mur.append((i,13))
    for j in range(4,7):
        murs.append(TERRAIN.create_rectangle(12*30,j*30,30+12*30,(j+1)*30,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(570,j*30,600,(j+1)*30,fill='#814436'))
        coordonnees_mur.append((12,j))
        coordonnees_mur.append((19,j))

def murs_4():
    global murs
    global TERRAIN
    for i in range(3,6):
        murs.append(TERRAIN.create_rectangle(i*30,6*30,(i+1)*30,30+6*30,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(i*30,390,(i+1)*30,420,fill='#814436'))
        coordonnees_mur.append((i,6))
        coordonnees_mur.append((i,13))
    for j in range(6,11):
        murs.append(TERRAIN.create_rectangle(8*30,j*30,30+8*30,(j+1)*30,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(570,j*30,600,(j+1)*30,fill='#814436'))
        coordonnees_mur.append((8,j))
        coordonnees_mur.append((19,j))

def murs_5():
    global murs
    global TERRAIN
    for i in range(13,17):
        murs.append(TERRAIN.create_rectangle(i*30,10*30,(i+1)*30,30+10*30,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(i*30,390,(i+1)*30,420,fill='#814436'))
        coordonnees_mur.append((i,10))
        coordonnees_mur.append((i,13))

def fonction_mur_terrain():
    global coordonnees_mur
    global murs
    if variable_mur == 1:        
        murs = []
        coordonnees_mur = []
        fonction_mur()
        murs_2()
    elif variable_mur == 2:   
        murs = []
        coordonnees_mur = []
        fonction_mur()
        murs_3()
        murs_2()
    elif variable_mur == 3:      
        murs = []
        coordonnees_mur = []
        fonction_mur()
        murs_3()
        murs_2()
        murs_4()
        murs_5()

def demarrer():
    """fonction qui commence le jeu avec un serpent au milieu"""   
    global serpent
    global coordonnees_serpent
    global direction
    global score

    serpent = []
    coordonnees_serpent = []
    direction = 0
    score = 0

    serpent.extend(
    [TERRAIN.create_rectangle(300, 210, 330, 240, fill = "green", outline = 'grey20'),
    TERRAIN.create_rectangle(300, 210, 330, 240, fill = "green", outline = 'grey20'),
    TERRAIN.create_rectangle(300, 210, 330, 240, fill = "green", outline = 'grey20')]
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
        TERRAIN.create_rectangle(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))

        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i,j-1))
        del coordonnees_serpent[0]
        
        direction = "haut"

    elif buffer == "bas" :
        serpent.append(
        TERRAIN.create_rectangle(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))

        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i,j+1))
        del coordonnees_serpent[0]
        direction = "bas"


    elif buffer == "droite" :
        serpent.append(
        TERRAIN.create_rectangle(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))

        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i+1,j))
        del coordonnees_serpent[0]
        
        direction = "droite"


    elif buffer == "gauche" :
        serpent.append(
        TERRAIN.create_rectangle(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))
        
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
    l1=coordonnees_serpent[0:-3]

    #le serpent s'arrête lorsqu'il touche le mur
    if coordonnees_serpent[-1] in coordonnees_mur:
        game_over()
    
    #le serpent s'aggrandit quand il touche une pomme
    elif coordonnees_serpent[-2] in pomme:
        aggrandir_serpent()
        augmenter_score()
        creer_pommes()
        id_after = TERRAIN.after(vitesse_serpent,mouvement)

    #if case de devant est vide
    else:
        id_after = TERRAIN.after(vitesse_serpent, mouvement)


#################################################################################
# snake mange une pomme - creer nouvelle pomme - agrandir snake - augmenter score
# ecrire dans le fichier texte
#################################################################################

def augmenter_score():
    """augmente le score et change le texte indiquant le score"""
    global label_score
    global score

    score += 1
    label_score.config(text= "score : " + str(score))



#################################################################################
# ecriture dans le fichier texte
def liste():
    """fonction qui ajoute le nom et le score du joueur a la liste"""
    global pseudos_joueur
    global score
    global liste_username_score
    while pseudos_joueur != [] :
        liste_username_score.extend([[pseudos_joueur[0], score]])
        pseudos_joueur.remove(pseudos_joueur[0])
        score = 0

def score_trie(N):
    """clef pour tirer les scores par ordre croissant"""
    return N[1]

def liste_triee():
    """trie la liste des scores"""
    global liste_username_score
    liste_username_score = sorted(liste_username_score, reverse = True, key=score_trie)

def ecrire():
    """ecris la liste des scores dans le fichier texte"""
    global liste_username_score
    L = liste_username_score
    fic = open("tab_scores", "w")
    for i in range(20):
        if i % 2 == 1:
            fic.write("\n")
        else:
            fic.write(str(L[0][0]) + "\n" + str(L[0][1]) + "\n")
            fic.write(str(L[1][0]) + "\n" + str(L[1][1]) + "\n")
            fic.write(str(L[2][0]) + "\n" + str(L[2][1]) + "\n")
            fic.write(str(L[3][0]) + "\n" + str(L[3][1]) + "\n")
            fic.write(str(L[4][0]) + "\n" + str(L[4][1]) + "\n")
            fic.write(str(L[5][0]) + "\n" + str(L[5][1]) + "\n")
            fic.write(str(L[6][0]) + "\n" + str(L[6][1]) + "\n")
            fic.write(str(L[7][0]) + "\n" + str(L[7][1]) + "\n")
            fic.write(str(L[8][0]) + "\n" + str(L[8][1]) + "\n")
            fic.write(str(L[9][0]) + "\n" + str(L[9][1]) + "\n")
    fic.close()


def lire():
    """lis le fichier texte et crée le texte du tableau des scores"""
    global f
    j = 1
    i = 1
    fic = open("tab_scores","r")
    for ligne in fic:
        j *= -1
        if j == 1:
            i += 1
            label= tk.Label(f, text=(nom + ligne), font=("Helvetica", "10"), bg="dark green", fg="white")
            label.grid(row = i)
        elif j == -1:
            nom = ligne    
    fic.close()   

#################################################################################
 
def creer_pommes():
    """creation de pommes une fois que le serpent a mangé la première"""
    global POMME
    global coordonnees_mur
    i=rd.randint(1,18)
    j=rd.randint(1,12)

    #la pomme ne peut apparaître sur le corps du serpent
    if (i,j) in coordonnees_serpent:
        creer_pommes()
    
    #la pomme ne peut apparaître là où elle a disparu
    elif (i,j) == pomme[0]:
        creer_pommes()
    
    #la pomme ne peut apparaître dans les murs internes
    elif (i,j) in coordonnees_mur:
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
        TERRAIN.create_rectangle(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))
        coordonnees_serpent.insert(0,(i,j-1))


    elif direction == "bas" :
        serpent.insert(0,
        TERRAIN.create_rectangle(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))
        coordonnees_serpent.insert(0,(i,j+1))


    elif direction == "droite" :
        serpent.insert(0,
        TERRAIN.create_rectangle(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))
        coordonnees_serpent.insert(0,(i+1,j))

    elif direction == "gauche" :
        serpent.insert(0,
        TERRAIN.create_rectangle(i* 30, j * 30, i * 30+ 30, j * 30 + 30, fill = "green"))
        coordonnees_serpent.insert(0,(i-1,j))


#################################################################################
# snake prends un mur - game over
#################################################################################
""" attention fonction pas finies"""
def game_over():
    global id_after
    global id_text

    TERRAIN.after_cancel(id_after)
    id_text = []
    id_text.extend([TERRAIN.create_rectangle((160,175),(440,225), fill = "black"),
                    TERRAIN.create_text(300,200, text = "GAME OVER", fill = "red", font = ("Helvetica", 32))])
    
    demande_de_nom()



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
    "fonction qui demande une vitesse au joueur"
    global vitesse_serpent
    vitesse_serpent = demande_vitesse.get()
    demande_vitesse.delete(0,6)

def choix_vitesse():
    """choisit la vitesse du serpent"""
    global vitesse_serpent
    if (vit.get()==0):
        vitesse_serpent=700
    elif (vit.get()==1):
        vitesse_serpent=450
    elif (vit.get()==2):
        vitesse_serpent=200

def choix_niveau():
    """en attendant les fonctions de Hajar"""
    global variable_mur
    if (niv.get()==0):
        variable_mur=1
    elif (niv.get()==1):
        variable_mur=2
    elif (niv.get()==2):
        variable_mur=3

def demande_de_nom():
    "fonction qui ouvre une fenêtre qui demande le pseudo du joeur"
    demander_nom = tk.Tk()
    demander_nom.title("Le nom du joueur")

    def fermeture_fenetre(event):
        "fonction qui ferme la fenêtre si le joueur valide son pseudo"
        global pseudos_joueur
        transition_vers_menu()
        pseudos_joueur.append(Saisie_nom.get())
        Saisie_nom.delete(0,20)
        demander_nom.destroy()
        fenetre.withdraw()
        liste()
        liste_triee()
        ecrire()
        

    frame0 = tk.Frame(demander_nom, bg="dark green", padx=40, pady=40)
    frame0.pack()

    Label_nom = tk.Label(frame0,text="What's your username?",font=('Helvetica',15),bg='dark green', fg="chartreuse3")
    Label_instruction = tk.Label(frame0,text='20 characters only',font=('Helvetica',12),bg='dark green',fg='orange red')
    Label_instruction2 = tk.Label(frame0,text='Press Enter to confirm',font=('Helvetica',12),bg='dark green', fg="chartreuse3")
    Saisie_nom = tk.Entry(frame0, bg='dark green', fg='chartreuse3', width=20, font=('Helvetica',14))

    Label_nom.pack(pady=10)
    Saisie_nom.pack(pady=10)
    Label_instruction.pack(pady=5)
    Label_instruction2.pack(pady=5)

    demander_nom.bind('<KeyPress-Return>', fermeture_fenetre)
    demander_nom.mainloop()

    

#################################################################################
# fenetre des regles du jeu
#################################################################################

def comment_jouer():
    """fonction qui ouvre une fenetre d instructions"""
    fenetre = tk.Toplevel(root)
    fenetre.title("Les débuts")

#################################################################################
# fenetre du tableau des scores
#################################################################################

def scores():
    """fonction qui ouvre le tableau des scores et lis le fichier texte"""
    global f
    f = tk.Toplevel(root)
    f.title("Tableau des scores")
    f.geometry("500x600")

    fond_vert = tk.Canvas(f, bg = "dark green", height = 2000, width = 500)
    fond_vert.grid(rowspan=30, column = 0)
    label_titre =  tk.Label(f, text="Tableau des scores", font=("Helvetica", "20"), bg="dark green", fg="white")
    label_titre.grid(row = 0)

    lire()
 
#################################################################################
# fenetre snake
#################################################################################
def commencer():
    """fonction qui ouvre le jeu snake dans une fenetre a part"""
    global TERRAIN
    global label_score
    global fenetre

    #creation de la fenetre
    fenetre = tk.Toplevel(root)
    fenetre.title("SNAKE")

    #creation des widgets
    label_score= tk.Label(fenetre, text = "score : 0")
    label_score.grid(row = 0)
    TERRAIN = tk.Canvas(fenetre, height = HAUTEUR, width = LARGEUR, bg = "chartreuse3")
    TERRAIN.grid(row = 1)

    fenetre.bind("<KeyPress-Up>", haut)
    fenetre.bind("<KeyPress-Down>", bas)
    fenetre.bind("<KeyPress-Right>", droite)
    fenetre.bind("<KeyPress-Left>", gauche)
   
    #programme principal
    #quadrillage()
    demarrer()
    creer_premiere_pomme()
    fonction_mur()
    fonction_mur_terrain()



#################################################################################
#################################################################################
# creation du menu
#################################################################################
#################################################################################

root = tk.Tk()
root.geometry("700x600")
root.title("Menu")

frame_general = tk.Frame(root, bg="dark green", padx=50, pady=20)
frame_general.pack()

titre = tk.Label(frame_general, text="SNAKE", font=("Helvetica", "28", "bold"), bg="dark green", fg="chartreuse3")
titre.pack(anchor="n", pady=20)

###################################################################################################
# niveaux
###################################################################################################

titre_niveaux = tk.Label(frame_general, text="LEVELS", font=("Helvetica", "20", "bold"), bg="dark green", fg="chartreuse3")
titre_niveaux.pack(pady=40)

frame1 = tk.Frame(frame_general, bg="dark green")
frame1.pack()

niveaux = ["Level 1 : Easy", "Level 2 : Medium", "Level 3 : Hard"]

niv = tk.IntVar()

for index in range(len(niveaux)):
    radiobutton_niveaux = tk.Radiobutton(frame1, text=niveaux[index], 
                                    variable=niv, 
                                    value=index, 
                                    indicatoron=0, 
                                    command=choix_niveau,
                                    font=("Helvetica", "16", "bold"),
                                    bg="dark green",
                                    fg="chartreuse3")
    radiobutton_niveaux.pack(side="left", padx=20)

###################################################################################################
# vitesses
###################################################################################################

titre_vitesse = tk.Label(frame_general, text="SPEED", font=("Helvetica", "20", "bold"), bg="dark green", fg="chartreuse3")
titre_vitesse.pack(pady=40)

frame2 = tk.Frame(frame_general, bg="dark green")
frame2.pack()

vitesses = ["Slow", "Normal", "Fast"]

vit = tk.IntVar()

for index in range(len(niveaux)):
    radiobutton_vitesses = tk.Radiobutton(frame2, text=vitesses[index], 
                                    variable=vit, 
                                    value=index, 
                                    indicatoron=0, 
                                    command=choix_vitesse,
                                    font=("Helvetica", "16", "bold"),
                                    bg="dark green",
                                    fg="chartreuse3")
    radiobutton_vitesses.pack(side="left", padx=20)


###################################################################################################
# demande de la vitesse
###################################################################################################

frame3 = tk.Frame(frame_general, bg="dark green")
frame3.pack()

vitesse_personalisee = tk.Label(frame3, text="CHOOSE YOUR SPEED", font=("Helvetica", "20", "bold"), bg="dark green", fg="chartreuse3")
vitesse_personalisee.pack(pady=40)

demande_vitesse = tk.Entry(frame3, bg="dark green", fg="chartreuse3", font=("Helvetica", "14"))
demande_vitesse.pack(side="left")

unite_mouv = tk.Label(frame3, text='mvt/ms', font=('Helvetica', "16"), bg="dark green", fg="chartreuse3")
unite_mouv.pack(side="left")

frame4 = tk.Frame(frame_general, bg="dark green")
frame4.pack()

consigne = tk.Label(frame4, text="PRESS ENTER TO CONFIRM",font=("Helvetica", "8"), bg="dark green", fg="chartreuse3")
consigne.pack(anchor="s")


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