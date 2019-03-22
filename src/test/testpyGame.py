# -*- coding: utf-8 -*-
#helloworld.py
import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((500,400))

while(1):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()

