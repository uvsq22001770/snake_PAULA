FONCTIONNEMENT DU PROGRAMME


Vous êtes un serpent et votre but est de manger le plus de pommes possible.
Pour manger les pommes, vous vous déplacez grâce aux flèches du clavier dans les directions indiquées.
Pour pimenter la partie, vous grandissez d'une case à chaque pomme avalée et vous devez éviter des murs qui sont présents dans l'herbe ( leur nombre dépend du niveau de difficulté choisi au prélable ).
La partie se termine lorsque vous heurtez un mur ou mordez votre propre queue.

Vous pouvez également trouver ces informations dans le menu "Règles du jeu" une fois le programme lancé.

Lors du lancement du programme, vous avez accès à un menu qui vous donne le choix du niveau de difficulté du terrain ainsi que de votre vitesse ( vous pouvez également en saisir une vous-même ). Si vous entrez vous-même la vitesse, veillez à appuyer sur la touche "Enter" de votre clavier pour valider la saisie.

Le nombre de pommes que vous mangez est comptabilisé dans un fichier où seuls les scores des 10 meilleurs mangeurs apparaissent.
Une fenêtre demandant le nom du joueur apparaît à la fin de la partie. Pour valider la saisie, procédez comme précédemment, soit cliquez sur la touche "Enter".



PRECISIONS SUR LE PROGRAMME


La taille du terrain est à titre indicatif, le code fonctionne quelles que soient les dimensions choisies.

L'unité des vitesses a été choisie après reflexion au sujet de la cohérence des données : une vitesse en mouvements par seconde aurait donné suite à des valeurs numériques décimales, ce qui explique le choix d'une unité en millisecondes par mouvement.

L'apparence du jeu aurait pu être améliorée grâce à l'utilisation de la méthode Bitmap cependant elle n'a pas été appliquée par manque de temps.

Le jeu aurait pu être plus complet en ajoutant des fonctions qui augmenteraient la vitesse du serpent au cours du temps ou encore changeraient le serpent de niveau après un certain nombre de pommes avalées. Nous ne l'avons cependant pas fait car cela rendait le fait de tester le jeu plus compliqué mais également car ceci ne nous a pas été demandé.

Des fonctions de création des murs ont été jointes car elles avaient été faites avant la fonction de lecture du fichier contenant les niveaux. Puisque nous avons travaillé dessus, nous les avons jointes ci-dessous :


def fonction_mur():
    """Création des murs qui encadrent le terrain et le niveau 1"""

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
    """Création des murs du niveau 2"""

    global murs, TERRAIN

    for i in range(12,16):
        murs.append(TERRAIN.create_rectangle(i*coté,7*coté,(i+1)*coté,coté+7*coté,fill='#814436'))
        coordonnees_mur.append((i,7))
    
    for j in range(4,7):
        murs.append(TERRAIN.create_rectangle(12*coté,j*coté,coté+12*coté,(j+1)*coté,fill='#814436'))
        coordonnees_mur.append((12,j))


def murs_3():
    """Création des murs du niveau 3"""

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