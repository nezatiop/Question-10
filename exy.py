import pygame as pg, sys, math


pg.init()

#répertoire de couleur
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRIS = (128, 128, 128)
ORANGE = (255, 165, 0)
VIOLET = (128, 0, 128)
ROSE = (255, 182, 193)
BLEU_CIEL = (135, 206, 250)
VERT_FONCE = (0, 100, 0)

#screen
WIDTH, HEIGHT = 1000, 1000
fenetre = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Ma première application pygame")

clock = pg.time.Clock()

def dessiner_cercle(x, y, rayon, nb_cotes):
    for i in range(nb_cotes):
        angle1 = (2 * math.pi * i) / nb_cotes
        angle2 = (2 * math.pi * (i + 1)) / nb_cotes

        x1 = x + int(rayon * math.cos(angle1))
        y1 = y + int(rayon * math.sin(angle1))

        x2 = x + int(rayon * math.cos(angle2))
        y2 = y + int(rayon * math.sin(angle2))

        pg.draw.line(fenetre, BLANC, (x1, y1), (x2, y2), 1)

#vitesse du cercle
vitesseX = 1
vitesseY = 2

#centre du cercle
x_cercle = WIDTH//2
y_cercle = HEIGHT//2

rayon_cercle = 10

while True:
    clock.tick(144)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        

    fenetre.fill(NOIR)

    x_cercle += vitesseX
    y_cercle += vitesseY

    if x_cercle - rayon_cercle < 0 or x_cercle + rayon_cercle > WIDTH:
        vitesseX = -vitesseX

    if y_cercle - rayon_cercle < 0 or y_cercle + rayon_cercle > HEIGHT:
        vitesseY = -vitesseY


    dessiner_cercle(x_cercle, y_cercle, rayon_cercle, 100)


 
    pg.display.flip()

    pg.time.Clock().tick(60)


