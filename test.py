# from cheseBoard.preBoard import *
import cheseBoard.ASearchFinal
from cheseBoard.gVariables import CreateBoard, Piece,origin,end

myPiece = Piece(origin)# initialization my piece 
myBoard = CreateBoard(origin,end) # initialization my board
myBoard.placeBlock(1, 2, 3) 
myBoard.placeBlock(0, 3, 3)  
myBoard.placeBlock(1, 2, 2)

cheseBoard.ASearchFinal.searchPath(myPiece,myBoard)
print(myBoard.C) #print result 

"""
GUI
"""
# while(1):
#     textInit()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             sys.exit()
#         if event.type == pg.KEYDOWN:
#             if event.key == K_DOWN:
#                 Mychese.move(0,1)
#             elif event.key == K_UP:
#                 Mychese.move(0,-1)
#             elif event.key == K_LEFT:
#                 Mychese.move(-1,0)
#             elif event.key == K_RIGHT:
#                 Mychese.move(1,0)
#                 
#             elif event.key == K_s:
#                 Enemychese.move(0,1)
#             elif event.key == K_w:
#                 Enemychese.move(0,-1)
#             elif event.key == K_a:
#                 Enemychese.move(-1,0)
#             elif event.key == K_d:
#                 Enemychese.move(1,0)
#     pg.display.update()
# pg.quit()
