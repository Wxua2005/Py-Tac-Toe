import pygame
import sys
import random
import time

pygame.init()
screen = pygame.display.set_mode((800,500))
screen.fill('LightPink')
running = True
while running:
    rand_cord_x = random.randint(100,750)
    rand_cord_y = random.randint(100,750)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen,'Red',(rand_cord_x,rand_cord_y),5)

    pygame.display.update()