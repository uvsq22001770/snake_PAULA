##################################################################################
# groupe LDDMP 3
# Ismaël RAIS
# Ines ROSENTHAL
# Hajar ASBAI
# Adrien HANNA 
# Quentin ASSIE
# Paula POP
# https://github.com/uvsq22001770/Projet_2.git
##################################################################################

import tkinter as tk
import random as rd 

##################################################################################
##################################################################################
# CONSTANTES
##################################################################################
##################################################################################

coté = 30
LARGEUR= 20 * coté
HAUTEUR = 14 * coté
COULEUR_QUADR = "black"

##################################################################################
# définition des variables globales
##################################################################################

direction = 0
buffer = 0
score = 0
variable_mur = 1
variable_vitesse  = 1
vitesse_serpent = 700
murs = []
serpent = []
pomme = []
coordonnees_mur = []
coordonnees_serpent = []
pseudos_joueur = []
l1 = []
liste_vitesse = []
test_premiere_lecture = 0

liste_username_score=[ ["Username", 0], ["Username", 0],
   ["Username", 0], ["Username", 0], ["Username", 0], ["Username", 0],
   ["Username", 0], ["Username", 0], ["Username", 0] ]


##################################################################################
##################################################################################
# FONCTIONS
##################################################################################
##################################################################################

def quadrillage():
    """Création du quadrillage ( qui disparaîtra par la suite )"""

    y = 0
    while y <= HAUTEUR:
        TERRAIN.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += coté
    x = 0
    while x <= LARGEUR:
        TERRAIN.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        x += coté

 
##################################################################################
# définition éléments du snake
##################################################################################


def creer_premiere_pomme():
    """Création de la première pomme du terrain"""
    
    global pomme
    global POMME
    global coordonnees_mur

    pomme = []
    POMME = []

    i = rd.randint(1,18)
    j = rd.randint(1,12)
    
    # la pomme ne peut pas apparaitre dans le serpent
    if (i,j) in coordonnees_serpent :
        creer_premiere_pomme()
    
    # la pomme ne peut pas apparaître sur un mur interne
    elif (i,j) in coordonnees_mur :
        creer_premiere_pomme()
    
    else:
        pomme.append((i, j))
        POMME=TERRAIN.create_oval(i*coté, j*coté, (i*coté) + coté, (j*coté) + coté, fill = "red")


def creer_pommes():
    """Création des pommes une fois que le serpent a mangé la première"""

    global POMME
    global coordonnees_mur

    i = rd.randint(1,18)
    j = rd.randint(1,12)

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
        POMME=TERRAIN.create_oval(i*coté, j*coté, (i*coté)+coté, (j*coté)+coté, fill = "red")


def fonction_mur():
    """Création des murs qui encadrent le terrain et le niveau 1"""

    global murs, TERRAIN

    fic = open("niveau 1", "r")
    for ligne in fic :
       var = ligne
       liste = var.split(",")
       (i, j) = (int(liste[0]), int(liste[1]))  
       murs.append(TERRAIN.create_rectangle(i*coté,j*coté,(i+1)*coté,(j+1)*coté,fill='#814436'))
       coordonnees_mur.append((i,j)) 


def murs_2():
    """Création des murs du niveau 2"""

    global murs, TERRAIN

    fic = open("niveau 2", "r")
    for ligne in fic :
       var = ligne
       liste = var.split(",")
       (i, j) = (int(liste[0]), int(liste[1]))  
       murs.append(TERRAIN.create_rectangle(i*coté,j*coté,(i+1)*coté,(j+1)*coté,fill='#814436'))
       coordonnees_mur.append((i,j)) 


def murs_3():
   """Création des murs du niveau 3"""

   global murs, TERRAIN

   fic = open("niveau 3", "r")
   for ligne in fic :
       var = ligne
       liste = var.split(",")
       (i, j) = (int(liste[0]), int(liste[1]))  
       murs.append(TERRAIN.create_rectangle(i*coté,j*coté,(i+1)*coté,(j+1)*coté,fill='#814436'))
       coordonnees_mur.append((i,j)) 
    

def gestion_mur_terrain():
    """Associe le choix du niveau aux fonctions de création des murs"""

    global coordonnees_mur
    global murs

    if variable_mur == 1:        
        murs = []
        coordonnees_mur = []
        fonction_mur()
    elif variable_mur == 2:   
        murs = []
        coordonnees_mur = []
        fonction_mur()
        murs_2()
    elif variable_mur == 3:      
        murs = []
        coordonnees_mur = []
        fonction_mur()
        murs_2()
        murs_3()


def demarrer():
    """Fonction qui commence le jeu avec un serpent au milieu"""

    global serpent
    global coordonnees_serpent
    global direction
    global score

    serpent = []
    coordonnees_serpent = []
    direction = 0
    score = 0

    serpent.extend(
    [TERRAIN.create_rectangle(10 * coté, 7 * coté, 10 * coté+ coté, 7 * coté + coté, fill = "green", outline = 'green'),
    TERRAIN.create_rectangle(10 * coté, 7 * coté, 10 * coté+ coté, 7 * coté + coté, fill = "green", outline = 'green'),
    TERRAIN.create_rectangle(10 * coté, 7 * coté, 10 * coté+ coté, 7 * coté + coté, fill = "green", outline = 'green')]
    )
    coordonnees_serpent=[(10,7),(10,7),(10,7)]
    mouvement()


##################################################################################
# fonctions mouvements du serpent
##################################################################################


def haut(event):
    """Déplace le serpent vers le haut"""
    global buffer
    if direction != "bas":
        buffer = "haut"


def bas(event):
    """Déplace le serpent vers le bas"""
    global buffer
    if direction != "haut":
        buffer = "bas"


def droite(event):
    """Déplace le serpent vers la droite"""
    global buffer
    if direction != "gauche":
        buffer = "droite"


def gauche(event):
    """Déplace le serpent vers la gauche"""
    global buffer
    if direction != "droite":
        buffer = "gauche"


def etape_mouvement(i,j):
    """Fonction qui fait bouger le serpent d'une case dans la direction indiquée"""

    global direction
    global coordonnees_serpent


    if buffer == 0 :
        pass

    elif buffer == "haut" :
        serpent.append(
        TERRAIN.create_rectangle(i* coté, j * coté, i * coté+ coté, j * coté + coté, fill = "green", outline = 'green'))
        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i,j-1))
        del coordonnees_serpent[0]
        direction = "haut"

    elif buffer == "bas" :
        serpent.append(
        TERRAIN.create_rectangle(i* coté, j * coté, i * coté+ coté, j * coté + coté, fill = "green", outline = 'green'))
        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i,j+1))
        del coordonnees_serpent[0]
        direction = "bas"

    elif buffer == "droite" :
        serpent.append(
        TERRAIN.create_rectangle(i* coté, j * coté, i * coté+ coté, j * coté + coté, fill = "green", outline = 'green'))
        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i+1,j))
        del coordonnees_serpent[0]
        direction = "droite"

    elif buffer == "gauche" :
        serpent.append(
        TERRAIN.create_rectangle(i* coté, j * coté, i * coté+ coté, j * coté + coté, fill = "green", outline = 'green'))
        TERRAIN.delete(serpent[0])
        del serpent[0]
        coordonnees_serpent.append((i-1,j))
        del coordonnees_serpent[0]
        direction = "gauche"


def mouvement():
    """Fonction qui fait bouger le serpent et fait le test en cas de victoire ou défaite"""

    global id_after
    l1 = coordonnees_serpent[0:-3]
    (i,j) = coordonnees_serpent[-1]
    etape_mouvement(i,j)

    # le serpent s'arrête lorsqu'il touche le mur
    if coordonnees_serpent[-1] in coordonnees_mur:
        TERRAIN.after(1, game_over)
    
    # le serpent s'arrête lorsqu'il se touche lui même
    elif coordonnees_serpent[-1] in l1 :
        TERRAIN.after(1, game_over)
     
    # le serpent s'aggrandit lorsqu'il touche une pomme
    if coordonnees_serpent[-2] in pomme:
        aggrandir_serpent()
        augmenter_score()
        creer_pommes()
        id_after = TERRAIN.after(vitesse_serpent, mouvement)

    # si la case de devant est vide
    else:
        id_after = TERRAIN.after(vitesse_serpent, mouvement)


def aggrandir_serpent():
    """Le corps du serpent s'aggrandit d'un rectangle"""

    (i,j)=coordonnees_serpent[0]
    
    if direction==0 :
        pass

    elif direction == "haut" :
        serpent.insert(0,
        TERRAIN.create_rectangle(i* coté, j * coté, i * coté+ coté, j * coté + coté, fill = "green", outline = 'green'))
        coordonnees_serpent.insert(0,(i,j-1))

    elif direction == "bas" :
        serpent.insert(0,
        TERRAIN.create_rectangle(i* coté, j * coté, i * coté+ coté, j * coté + coté, fill = "green", outline = 'green'))
        coordonnees_serpent.insert(0,(i,j+1))

    elif direction == "droite" :
        serpent.insert(0,
        TERRAIN.create_rectangle(i* coté, j * coté, i * coté+ coté, j * coté + coté, fill = "green", outline = 'green'))
        coordonnees_serpent.insert(0,(i+1,j))

    elif direction == "gauche" :
        serpent.insert(0,
        TERRAIN.create_rectangle(i* coté, j * coté, i * coté+ coté, j * coté + coté, fill = "green", outline = 'green'))
        coordonnees_serpent.insert(0,(i-1,j))


##################################################################################
# fonctions game over : si snake rentre dans un mur ou se mord la queue
##################################################################################


def game_over():
    """Affiche le message game over sur snake et ouvre la fenetre qui demande le nom"""

    global id_after
    global id_text

    TERRAIN.after_cancel(id_after)
    id_text = []
    id_text.extend([TERRAIN.create_rectangle((coté * 160 //30,coté * 175 //30),
                                            (coté * 440 //30, coté * 225 //30), fill = "black"),
                    TERRAIN.create_text(coté * 300 //30,coté * 200 //30, text = "GAME OVER",
                                        fill = "red", font = ("Helvetica", coté + 2))])
    
    demande_de_nom()


def transition_vers_menu():
    """Supprime toutes les variables de snake"""

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


##################################################################################
# fonctions liées au score et à son écriture dans un fichier
##################################################################################


def augmenter_score():
    """augmente le score et change le texte indiquant le score"""

    global label_score
    global score

    score += 1
    label_score.config(text= "score : " + str(score))


def premiere_lecture():
    """Première lecture du fichier texte s'il existe"""

    global test_premiere_lecture

    if test_premiere_lecture == 0 :
        test_premiere_lecture = 1
        fic = open("tab_scores", "r")
        j = 1
        for ligne in fic:
            j *= -1
            if j == -1 :
                var = ligne 
                liste = var.split("\n")
                nom = liste[0]
                
            elif j == 1 :
                liste_username_score.append([nom, int(ligne)])


def liste():
    """Fonction qui ajoute le nom et le score du joueur à la liste"""

    global pseudos_joueur
    global score
    global liste_username_score

    while pseudos_joueur != [] :
        liste_username_score.extend([[pseudos_joueur[0], score]])
        pseudos_joueur.remove(pseudos_joueur[0])
        score = 0


def score_trie(N):
    """Clé pour tirer les scores par ordre croissant"""

    return N[1]


def liste_triee():
    """Trie la liste des scores"""

    global liste_username_score

    liste_username_score = sorted(liste_username_score, reverse = True, key=score_trie)


def ecrire():
    """Ecrit la liste des scores dans le fichier texte"""

    global liste_username_score

    L = liste_username_score
    fic = open("tab_scores", "w")
    for i in range(20):
        if i % 2 == 0: 
            fic.write(str(L[i//2][0]) + "\n" + str(L[i//2][1]) + "\n")
    fic.close()


def lire():
    """Lit le fichier texte et crée le texte du tableau des scores"""

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


##################################################################################
##################################################################################
# MENU
##################################################################################
##################################################################################

def valider(event):
    "Fonction qui demande une vitesse au joueur"

    global vitesse_serpent
    global liste_vitesse

    vitesse_serpent_test = demande_vitesse.get()

    if vitesse_serpent_test.isdigit():
        if float(vitesse_serpent_test) == float(200):
            vitesse_serpent = demande_vitesse.get()
            demande_vitesse.delete(0,6)
            valeur_vitesse['text'] = str(vitesse_serpent) +' ms/mvt'
            liste_vitesse[2].select()
        elif float(vitesse_serpent_test) == float(450):
            vitesse_serpent = demande_vitesse.get()
            demande_vitesse.delete(0,6)
            liste_vitesse[1].select()
            valeur_vitesse['text'] = str(vitesse_serpent) +' ms/mvt'
        elif float(vitesse_serpent_test) == float(700):
            vitesse_serpent = demande_vitesse.get()
            demande_vitesse.delete(0,6)
            liste_vitesse[0].select()
            valeur_vitesse['text'] = str(vitesse_serpent) +' ms/mvt'
        else:
            vitesse_serpent = demande_vitesse.get()
            demande_vitesse.delete(0,6)
            valeur_vitesse['text'] = str(vitesse_serpent) +' ms/mvt'
            deselectionner()
    else:
        demande_vitesse.delete(0,6)
        

def choix_vitesse():
    """Attribue une vitesse au serpent"""

    global vitesse_serpent
    global variable_vitesse

    if (vit.get()==0):
        vitesse_serpent=700
        variable_vitesse=1
        valeur_vitesse['text'] = str(vitesse_serpent) +' ms/mvt'
    elif (vit.get()==1):
        vitesse_serpent=450
        variable_vitesse=2
        valeur_vitesse['text'] = str(vitesse_serpent) +' ms/mvt'
    elif (vit.get()==2):
        vitesse_serpent=200
        variable_vitesse=3
        valeur_vitesse['text'] = str(vitesse_serpent) +' ms/mvt'


def choix_niveau():
    """Intègre des murs à l'intérieur du terrain selon le niveau de difficulté"""

    global variable_mur

    if (niv.get()==0):
        variable_mur=1
    elif (niv.get()==1):
        variable_mur=2
    elif (niv.get()==2):
        variable_mur=3


def deselectionner():
    """Déselectionne les boutons enclenchés"""

    global variable_vitesse

    if variable_vitesse == 1:
        liste_vitesse[0].deselect()
    elif variable_vitesse == 2:
        liste_vitesse[1].deselect()
    elif variable_vitesse == 3:
        liste_vitesse[2].deselect()


def demande_de_nom():
    "Fonction qui ouvre une fenêtre qui demande le pseudo du joueur"

    demander_nom = tk.Tk()
    demander_nom.title("Player's name")

    def fermeture_fenetre(event):
        "Fonction qui ferme la fenêtre si le joueur valide son pseudo"

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
    Label_instruction = tk.Label(frame0,text='20 characters only',font=('Helvetica',12),bg='dark green',fg='chartreuse3')
    Label_instruction2 = tk.Label(frame0,text='PRESS ENTER TO CONFIRM',font=('Helvetica',8),bg='dark green', fg="chartreuse3")
    Saisie_nom = tk.Entry(frame0, bg='dark green', fg='chartreuse3', width=20, font=('Helvetica',14))

    Label_nom.pack(pady=10)
    Saisie_nom.pack(pady=10)
    Label_instruction.pack(pady=5)
    Label_instruction2.pack(pady=5)

    demander_nom.bind('<KeyPress-Return>', fermeture_fenetre)
    demander_nom.mainloop()


##################################################################################
# fenêtre des règles du jeu
##################################################################################


def comment_jouer():
    """Fonction qui ouvre une fenêtre d'instructions"""

    f1 = tk.Toplevel(root)
    f1.title("Règles du jeu")
    f1.geometry("768x550")
    f1.resizable(height=False, width=False)

    rule = tk.Frame(f1, bg="dark green", padx=40, pady=40)
    rule.pack()

    regles_jeu = tk.Label(rule, text="Règles du jeu", font=("Helvetica", "20", "bold"), bg="dark green", fg="chartreuse3")
    mouvement_serpent = tk.Label(rule, text="Comment déplacer le serpent",
                                font=("Helvetica", "12", "bold"), bg="dark green", fg="chartreuse3")
    deplacement_droite = tk.Label(rule, text="Pour se déplacer à droite : cliquer sur la flèche de droite",
                                font=("Helvetica", "10"), bg="dark green", fg="chartreuse3")
    deplacement_gauche = tk.Label(rule, text="Pour se déplacer à gauche : cliquer sur la flèche de gauche",
                                font=("Helvetica", "10"), bg="dark green", fg="chartreuse3")
    deplacement_haut = tk.Label(rule, text="Pour se déplacer vers le haut : cliquer sur la flèche du haut",
                                font=("Helvetica", "10"), bg="dark green", fg="chartreuse3")
    deplacement_bas = tk.Label(rule, text="Pour se déplacer vers le bas : cliquer sur la flèche du bas",
                                font=("Helvetica", "10"), bg="dark green", fg="chartreuse3")

    rule.pack()
    regles_jeu.pack(pady=15)
    mouvement_serpent.pack(pady=30)
    deplacement_droite.pack()
    deplacement_gauche.pack()
    deplacement_haut.pack()
    deplacement_bas.pack()

    texte_consigne = tk.Label(rule, text="Règles du jeu",
                                font=("Helvetica", "12", "bold"), bg="dark green", fg="chartreuse3")
    consigne = tk.Label(rule, text="Le but est de manger la pomme.",
                                font=("Helvetica", "10"), bg="dark green", fg="chartreuse3")

    consigne_1 = tk.Label(rule, text="Lorsqu’elle est mangée, une autre pomme apparaît sur une case aléatoire du plateau, et le serpent grandit d'une case.",
                                font=("Helvetica", "10"), bg="dark green", fg="chartreuse3")

    consigne_2 = tk.Label(rule, text="La partie s’arrête lorsque la tête du serpent percute un mur ou percute son propre corps.",
                                font=("Helvetica", "10"), bg="dark green", fg="chartreuse3")

    encouragement = tk.Label(rule, text="Bonne chance ;)",
                                font=("Helvetica", "12", "bold"), bg="dark green", fg="chartreuse3")

    texte_consigne.pack(pady=30)
    consigne.pack()
    consigne_1.pack()
    consigne_2.pack()
    encouragement.pack(pady=30)

    f1.mainloop()


##################################################################################
# fenêtre du tableau des scores
##################################################################################


def scores():
    """Fonction qui ouvre le tableau des scores et lit le fichier texte"""

    global f

    f = tk.Toplevel(root)
    f.title("Tableau des scores")
    f.geometry("500x600")

    fond_vert = tk.Canvas(f, bg = "dark green", height = 600, width = 500)
    fond_vert.grid(rowspan=12, column = 0)
    label_titre =  tk.Label(f, text="Tableau des scores", font=("Helvetica", "20"), bg="dark green", fg="white")
    label_titre.grid(row = 0)

    lire()


##################################################################################
# fenêtre snake
##################################################################################


def bouton_commencer(event):
    """Demarre snake en vitess rapide en appuyant sur espace"""

    global vitesse_serpent

    vitesse_serpent = 200
    variable_vitesse = 3
    deselectionner()
    valeur_vitesse['text'] = str(vitesse_serpent) +' ms/mvt'
    commencer()


def commencer():
    """Fonction qui ouvre le jeu snake dans une fenêtre à part"""

    global TERRAIN
    global label_score
    global fenetre

    fenetre = tk.Toplevel(root)
    fenetre.title("SNAKE")

    label_score= tk.Label(fenetre, text = "score : 0")
    label_score.grid(row = 0)
    TERRAIN = tk.Canvas(fenetre, height = HAUTEUR, width = LARGEUR, bg = "chartreuse3")
    TERRAIN.grid(row = 1)

    fenetre.bind("<KeyPress-Up>", haut)
    fenetre.bind("<KeyPress-Down>", bas)
    fenetre.bind("<KeyPress-Right>", droite)
    fenetre.bind("<KeyPress-Left>", gauche)

    #quadrillage() #(la fonction peut etre ajoutée ici pour faire apparaitre le quadrillage)
    demarrer()
    gestion_mur_terrain()
    creer_premiere_pomme()
    premiere_lecture()


##################################################################################
##################################################################################
# PROGRAMME PRINCIPAL
##################################################################################
##################################################################################


root = tk.Tk()
root.geometry("700x660")
root.title("Menu")

frame_general = tk.Frame(root, bg="dark green", padx=50, pady=20)
frame_general.pack()

titre = tk.Label(frame_general, text="SNAKE", font=("Helvetica", "28", "bold"), bg="dark green", fg="chartreuse3")
titre.pack(anchor="n", pady=20)


##################################################################################
# niveaux
##################################################################################


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


##################################################################################
# vitesses
##################################################################################


titre_vitesse = tk.Label(frame_general, text="SPEED", font=("Helvetica", "20", "bold"), bg="dark green", fg="chartreuse3")
titre_vitesse.pack(pady=40)

frame2 = tk.Frame(frame_general, bg="dark green")
frame2.pack()

vitesses = ["Slow", "Normal", "Fast"]

vit = tk.IntVar()

for index in range(len(vitesses)):
    radiobutton_vitesses=tk.Radiobutton(frame2, text=vitesses[index], 
                                    variable=vit, 
                                    value=index, 
                                    indicatoron=0, 
                                    command=choix_vitesse,
                                    font=("Helvetica", "16", "bold"),
                                    bg="dark green",
                                    fg="chartreuse3")
    radiobutton_vitesses.pack(side="left", padx=20)
    liste_vitesse.append(tk.Radiobutton(frame2, text=vitesses[index], 
                                    variable=vit, 
                                    value=index, 
                                    indicatoron=0, 
                                    command=choix_vitesse,
                                    font=("Helvetica", "16", "bold"),
                                    bg="dark green",
                                    fg="chartreuse3"))


##################################################################################
# demande de la vitesse
##################################################################################


frame3 = tk.Frame(frame_general, bg="dark green")
frame3.pack()

vitesse_personalisee = tk.Label(frame3, text="CHOOSE YOUR SPEED", font=("Helvetica", "20", "bold"), bg="dark green", fg="chartreuse3")
vitesse_personalisee.pack(pady=40)

consigne = tk.Label(frame3, text="PRESS ENTER TO CONFIRM",font=("Helvetica", "8"), bg="dark green", fg="chartreuse3")
consigne.pack(side="top",anchor='s')

demande_vitesse = tk.Entry(frame3, bg="dark green", fg="chartreuse3", font=("Helvetica", "14"))
demande_vitesse.pack(side="left")

unite_mouv = tk.Label(frame3, text='ms/mvt', font=('Helvetica', "16"), bg="dark green", fg="chartreuse3")
unite_mouv.pack(side="left")

frame4 = tk.Frame(frame_general, bg="dark green")
frame4.pack()

donne_vitesse = tk.Label(frame4, text='CURRENT SPEED:', font=('Helvetica','16'), bg="dark green", fg='chartreuse3')
donne_vitesse.pack(pady=15,side='left')

valeur_vitesse = tk.Label(frame4, text= str(vitesse_serpent) + ' ms/mvt', font=('Helvetica','16'), bg="dark green", fg='chartreuse3')
valeur_vitesse.pack(pady=15)


##################################################################################
# widgets du menu déroulant
##################################################################################


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


##################################################################################
# gestion des évènements
##################################################################################


root.bind("<KeyPress-Up>", haut)
root.bind("<KeyPress-Down>", bas)
root.bind("<KeyPress-Right>", droite)
root.bind("<KeyPress-Left>", gauche)
root.bind('<KeyPress-Return>',valider)
root.bind('<KeyPress-space>',bouton_commencer)

root.config(menu=mainmenu)
root.mainloop()
