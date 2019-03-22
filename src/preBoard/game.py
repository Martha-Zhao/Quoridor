'''


@author: Martha Zhao
'''
import pygame as pg,sys

screen = pg.display.set_mode((1024,768))
pg.init()
# def peredit():
#     
back = pg.image.load("back.jpg")
screen.fill((0,0,0))
screen.blit(back,(0,0))
#     for i in range (0,7):
#         for j in range(0,7):
#             pg.draw.rect(screen,[100,10,255],[i*80 + 20,j*80 + 20,60,60])
#            
#     pg.draw.circle(screen,[255,100,100],[290,50],30,0)
#     pg.draw.circle(screen,[255,255,100],[290,530],30,0) 
#     pg.display.update()
#     
# peredit()


def textShow(text):
    cur_font = pg.font.SysFont("arial", 16)
    myBlockString = cur_font.render(str(text), True, (255,255,255))
    screen.blit(myBlockString,(700,50))

temp= 10
myFont = pg.font.SysFont("arial",16)
myBlockNumText = myFont.render("My Blocks : ", True, (255,255,255))
myBlockString = myFont.render(str(temp), True, (255,255,255))
screen.blit(myBlockNumText,(570,50))
# screen.blit(myBlockString,(700,50))

while(1):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    for  i in range(10):
        textShow(i)
        pg.display.flip()
        pg.time.wait(500)
        



