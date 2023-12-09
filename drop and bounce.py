import pygame
import sys
import math
import random
pygame.init()

largeur, hauteur = 600, 800
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Boucing Balls")

blanc = (255, 255, 255)
bleu = (0, 0, 255)
couleur = bleu
positions_clics = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            couleur = bleu
            positions_clics.append(list(event.pos) + [20, 20])  # [x, y, vx, vy]

    fenetre.fill(blanc)

    for i, pos1 in enumerate(positions_clics):
        x1, y1, vx1, vy1 = pos1
        
        # Déplacement du cercle
        x1 += vx1
        y1 += vy1

        # Rebondir lorsque le cercle touche les bords de la fenêtre
        if x1 < 0 or x1 > largeur:
            vx1 = -vx1
        if y1 < 0 or y1 > hauteur:
            vy1 = -vy1

        # Vérifier les collisions avec les autres cercles
        for j, pos2 in enumerate(positions_clics):
            if i != j:  # Éviter la comparaison avec lui-même
                x2, y2, vx2, vy2 = pos2
                distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                somme_rayons = 20  # Changer cela en fonction de la taille de vos cercles
                if distance < somme_rayons:
                    # Collision détectée, ajuster les vitesses des deux cercles
                    vx1, vy1, vx2, vy2 = -vx2, -vy2, -vx1, -vy1
                    couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pos1[0], pos1[1], pos1[2], pos1[3] = x1, y1, vx1, vy1
        
        pygame.draw.circle(fenetre, couleur, (int(x1), int(y1)), 10)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
