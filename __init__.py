#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Mon Mar  4 15:17:45 2019

@author: martha
"""

import pygame as pg, sys
from pygame.locals import *
import os
 
from cheseBoard.preBoard import *

while(1):
    textInit()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == K_DOWN:
                Mychese.move(0,1)
            elif event.key == K_UP:
                Mychese.move(0,-1)
            elif event.key == K_LEFT:
                Mychese.move(-1,0)
            elif event.key == K_RIGHT:
                Mychese.move(1,0)
                
            elif event.key == K_s:
                Enemychese.move(0,1)
            elif event.key == K_w:
                Enemychese.move(0,-1)
            elif event.key == K_a:
                Enemychese.move(-1,0)
            elif event.key == K_d:
                Enemychese.move(1,0)
    pg.display.update()
pg.quit()
