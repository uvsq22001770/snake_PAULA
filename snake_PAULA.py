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
#########################################
# définition des constantes
#########################################
#########################################

coté = 30
LARGEUR= 20 * coté
HAUTEUR = 14 * coté
COULEUR_QUADR = "grey60"

#########################################
# définition des variables globales
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
# debut du snake- pomme - murs - serpent
#################################################################################

def creer_premiere_pomme():
    """creation de la premiere pomme du terrain"""
    global pomme
    global POMME
    global coordonnees_mur

    pomme = []
    POMME = []

    i = rd.randint(1,18)
    j = rd.randint(1,12)
    
    #la pomme ne peut pas apparaitre dans le serpent
    if (i,j) in coordonnees_serpent :
        creer_premiere_pomme()
    
    #la pomme ne peut pas apparaître sur un mur interne
    elif (i,j) in coordonnees_mur :
        creer_premiere_pomme()
    
    else:
        pomme.append((i, j))
        POMME=TERRAIN.create_oval(i*coté, j*coté, (i*coté) + coté, (j*coté) + coté, fill = "red")


def fonction_mur():
    """creation des murs qui encadrent le terrain et du niveau 1"""
    global murs, TERRAIN
    for i in range(1,19):
        murs.append(TERRAIN.create_rectangle(i*coté,0,(i+1)*coté,coté,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(i*coté,13*coté,(i+1)*coté,13 *coté + coté,fill='#814436'))
        coordonnees_mur.append((i,0))
        coordonnees_mur.append((i,13))
    for i in range(5,13):
        murs.append(TERRAIN.create_rectangle(i*coté,3*coté,(i+1)*coté,coté*3+coté,fill='#814436'))
        coordonnees_mur.append((i,3))
    for j in range(14):
        murs.append(TERRAIN.create_rectangle(0,j*coté,coté,(j+1)*coté,fill='#814436'))
        murs.append(TERRAIN.create_rectangle(19 * coté,j*coté,19*coté+coté,(j+1)*coté,fill='#814436'))
        coordonnees_mur.append((0,j))
        coordonnees_mur.append((19,j))
    for j in range(4,6):
        murs.append(TERRAIN.create_rectangle(5*coté,j*coté,coté+5*coté,(j+1)*coté,fill='#814436'))
        coordonnees_mur.append((5,j))
  
def murs_2():
    """creation des murs du niveau 2"""
    global murs, TERRAIN
    for i in range(12,16):
        murs.append(TERRAIN.create_rectangle(i*coté,7*coté,(i+1)*coté,coté+7*coté,fill='#814436'))
        coordonnees_mur.append((i,7))
    for j in range(4,7):
        murs.append(TERRAIN.create_rectangle(12*coté,j*coté,coté+12*coté,(j+1)*coté,fill='#814436'))
        coordonnees_mur.append((12,j))

def murs_3():
    """creation des murs du niveau 3"""
    global murs, TERRAIN
    for i in range(3,6):
        murs.append(TERRAIN.create_rectangle(i*coté,6*coté,(i+1)*coté,coté+6*coté,fill='#814436'))
        coordonnees_mur.append((i,6))
    for i in range(13,17):
        murs.append(TERRAIN.create_rectangle(i*coté,10*coté,(i+1)*coté,coté+10*coté,fill='#814436'))
        coordonnees_mur.append((i,10))
    for j in range(6,11):
        murs.append(TERRAIN.create_rectangle(8*coté,j*coté,coté+8*coté,(j+1)*coté,fill='#814436'))
        coordonnees_mur.append((8,j))
    

def gestion_mur_terrain():
    """fonction qui asocie le choix du niveau aux foncions de creation des murs"""
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
    [TERRAIN.create_rectangle(10 * coté, 7 * coté, 10 * coté+ coté, 7 * coté + coté, fill = "green", outline = 'green'),
    TERRAIN.create_rectangle(10 * coté, 7 * coté, 10 * coté+ coté, 7 * coté + coté, fill = "green", outline = 'green'),
    TERRAIN.create_rectangle(10 * coté, 7 * coté, 10 * coté+ coté, 7 * coté + coté, fill = "green", outline = 'green')]
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
    global l1
    global coordonnees_serpent

    l1 = coordonnees_serpent[0:-3]

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
    """fonction qui fait bouger le serpent et fait le test en cas de victoire/defaite"""
    global id_after
    (i,j) = coordonnees_serpent[-1]
    etape_mouvement(i,j)

    #le serpent s'arrête lorsqu'il touche le mur
    if coordonnees_serpent[-1] in coordonnees_mur:
        id_after = TERRAIN.after(1, game_over)
    
    #le serpent s'arrête lorsqu'il se touche lui même
    elif coordonnees_serpent[-1] in l1 :
        id_after = TERRAIN.after(1, game_over)
     
    #le serpent s'aggrandit quand il touche une pomme
    if coordonnees_serpent[-2] in pomme:
        aggrandir_serpent()
        augmenter_score()
        creer_pommes()
        id_after = TERRAIN.after(vitesse_serpent, mouvement)

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
def premiere_lecture():
    """premiere lecture du fichier texte si il existe"""
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
        if i % 2 == 0: 
            fic.write(str(L[i//2][0]) + "\n" + str(L[i//2][1]) + "\n")
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



def aggrandir_serpent():
    """le corps du serpent s'aggrandit d'un rectangle"""
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


#################################################################################
# snake prends un mur - game over
#################################################################################

def game_over():
    """affiche le message game over sur snake et ouvre la fenetre qui demande le nom """
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
    """supprime toutes les variables de snake"""
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
    """#attention pas de docstring"""
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
    """intègre des murs à l'interieur du terrain selon le niveau de difficulté"""
    global variable_mur
    if (niv.get()==0):
        variable_mur=1
    elif (niv.get()==1):
        variable_mur=2
    elif (niv.get()==2):
        variable_mur=3

def deselectionner():
    """#attention pas de docstring"""
    global variable_vitesse
    if variable_vitesse == 1:
        liste_vitesse[0].deselect()
    elif variable_vitesse == 2:
        liste_vitesse[1].deselect()
    elif variable_vitesse == 3:
        liste_vitesse[2].deselect()


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
    """fonction qui ouvre une fenetre d'instructions"""
    f1 = tk.Toplevel(root)
    f1.title("Règles du jeu")
    f1.geometry("815x550")
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

    consigne_1 = tk.Label(rule, text="Lorsqu’elle est mangée, une autre pomme apparaît sur une case aléatoire du plateau, et la longueur du serpent augmente de 1.",
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

#################################################################################
# fenetre du tableau des scores
#################################################################################

def scores():
    """fonction qui ouvre le tableau des scores et lis le fichier texte"""
    global f
    f = tk.Toplevel(root)
    f.title("Tableau des scores")
    f.geometry("500x600")

    fond_vert = tk.Canvas(f, bg = "dark green", height = 600, width = 500)
    fond_vert.grid(rowspan=12, column = 0)
    label_titre =  tk.Label(f, text="Tableau des scores", font=("Helvetica", "20"), bg="dark green", fg="white")
    label_titre.grid(row = 0)

    lire()
 
#################################################################################
# fenetre snake
#################################################################################
def bouton_commencer(event):
    """fonction qui lie la pression sur espace et la fonction commencer"""
    global vitesse_serpent
    vitesse_serpent=200
    variable_vitesse=3
    deselectionner()
    valeur_vitesse['text'] = str(vitesse_serpent) +' ms/mvt'
    commencer()

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
    fonction_mur()
    gestion_mur_terrain()
    creer_premiere_pomme()
    premiere_lecture()



#################################################################################
#################################################################################
# programe principal - creation du menu
#################################################################################
#################################################################################

root = tk.Tk()
root.geometry("700x660")
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
#attention ce ne serait pas len(vitesse)??? ca ne change rien mais je crois que c est plus coherent?
for index in range(len(niveaux)):
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


###################################################################################################
# demande de la vitesse
###################################################################################################

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

donne_vitesse = tk.Label(frame4, text='VOTRE VITESSE EST DE:', font=('Helvetica','16'), bg="dark green", fg='orange red')
donne_vitesse.pack(pady=15,side='left')

valeur_vitesse = tk.Label(frame4, text= str(vitesse_serpent) + ' ms/mvt', font=('Helvetica','16'), bg="dark green", fg='orange red')
valeur_vitesse.pack(pady=15)

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
root.bind('<KeyPress-space>',bouton_commencer)

# boucle principale

root.config(menu=mainmenu)
root.mainloop()