#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Mon Mar  4 15:17:45 2019

@author: martha
"""

import pygame as pg, sys
from pygame.locals import *


class chese:
    def __init__(self,owner,x,y): #Iinital init
        self.owner = owner
        self.x = x
        self.y = y
        if self.owner:
            self.__color = [255,100,100]
        else:
            self.__color = [255,255,100]
            
    def move(self,x,y):
        pg.draw.circle(screen,[100,10,255],[self.x,self.y],30,0)
        self.x = self.x + x * 80
        self.y = self.y + y * 80
        pg.draw.circle(screen,self.__color,[self.x,self.y],30,0)
        pg.display.update()
    def pr(self): #print function
        print(self.owner,self.x,self.y)
        
class block:
    def __init__(self,owner):
        self.owner = owner#blocks'owner
        self.count = 10 #owner's bloks remain number  origin = 10
        if owner:
            self.__color = [255,100,100]
        else:
            self.__color = [255,255,100]
        
    def palce(self,mode,x,y): #1 vertical 0 horizon
        self.count = self.count - 1
        if mode:  #vertical
            self.x = 80 + (x - 1) * 80
            self.y = y * 80 + 20
            pg.draw.rect(screen,self.__color,[self.x,self.y,20,140])
        else:
            self.x = x * 80 + 20
            self.y = 80 + (y - 1) * 80
            pg.draw.rect(screen,self.__color,[self.x,self.y,140,20])
        pg.display.update()
        
Mychese = chese(bool(1),290,50)
Enemychese = chese(bool(0),290,530)        
Myblocks = block(bool(1))
Enemyblocks = block(bool(0)) 
     
screen = pg.display.set_mode((1024,768))
back = pg.image.load("back.jpg")

def textInit():
    myFont = pg.font.SysFont("arial",16)
    Caption = myFont.render("QUORIDOR", True, (255,255,255))
    myBlockNumText = myFont.render("My Blocks : ", True, (255,255,255))
    enemyBlockText = myFont.render("Enemy Blocks : ", True, (255,255,255))
    myBlockString = myFont.render(str(Myblocks.count), True, (255,255,255))
    enemyBlockString = myFont.render(str(Enemyblocks.count), True, (255,255,255))
    screen.blit(Caption,(250,0))
     
    screen.blit(myBlockNumText,(570,50))
    screen.blit(enemyBlockText,(570,530))
     
    screen.blit(myBlockString,(700,50))
    screen.blit(enemyBlockString,(700,530))
    
def peredit():
    pg.init()
#     screen.fill((0,0,0))
    screen.blit(back,(0,0))
    for i in range (0,7):
        for j in range(0,7):
            pg.draw.rect(screen,[100,10,255],[i*80 + 20,j*80 + 20,60,60])
           
    pg.draw.circle(screen,[255,100,100],[290,50],30,0)
    pg.draw.circle(screen,[255,255,100],[290,530],30,0)
    
    pg.display.update()
    
peredit()


