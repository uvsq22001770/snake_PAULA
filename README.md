# Projet_2

import tkinter as tk

LARGEUR = 600
HAUTEUR = 420


def comment_jouer():
    fenetre = tk.Toplevel(root)
    fenetre.title("Les débuts")


def commencer():
    fenetre = tk.Toplevel(root)
    fenetre.title("SNAKE")

    titre = tk.Label(fenetre, text="Commençons !")
    canvas = tk.Canvas(root, bg="dark green", fg="white", height=HAUTEUR, width=LARGEUR)

    phrase_niveau = tk.Label(fenetre, text="Tout d'abord, choisissez un niveau de jeu :")
    niveau_1 = tk.Button(fenetre, text="Niveau 1 : Easy")
    niveau_2 = tk.Button(fenetre, text="Niveau 2 : Medium")

    titre.grid()
    canvas.grid()
    phrase_niveau.grid(column=0, row=1, columnspan=3)
    niveau_1.grid(column=0, row=2)
    niveau_2.grid(column=1, row=2)



# création de la fenêtre + paramétrage
root = tk.Tk()
root.geometry("640x480")
root.title("Création du menu")

# widgets
mainmenu = tk.Menu(root)


regles = tk.Menu(mainmenu, tearoff=0)
regles.add_command(label="Comment jouer", command=comment_jouer)
regles.add_separator()
regles.add_command(label="Quitter", command=root.quit)

debut = tk.Menu(mainmenu, tearoff=0)
debut.add_command(label="Commencer", command=commencer)

mainmenu.add_cascade(label="Règles du jeu", menu=regles)
mainmenu.add_cascade(label="Commencer le jeu", menu=debut)

# boucle principale

root.config(menu=mainmenu)
root.mainloop()
