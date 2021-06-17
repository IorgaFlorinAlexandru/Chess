import pygame as pg

pg.font.init()

class Piece:
    def __init__(self, pieceName, pieceColor):
        self.pieceName = pieceName
        self.pieceColor = pieceColor
        self.firstMove = 0
    def drawPiece(self,X,Y,screen):
        pg.draw.rect(screen, (128,128,128), (X+20, Y+20, 40, 40))
        font=pg.font.SysFont('Comic Sans MS',10)
        text=font.render(self.pieceColor[0]+self.pieceName[0],1,(0,0,0) )
        screen.blit(text,(X+30,Y+30))
    def movePiece(self,board,boardX,boardY,pieceX,pieceY):
        if(self.pieceName == "Peon" ):
            if(self.pieceColor == "White"):
                if( self.firstMove == 0) :
                    if( pieceX == boardX and pieceY == boardY+1 and pieceY == boardY + 2):
                        self.firstMove = 1
                        return True
                else:
                    if( pieceX == boardX and pieceY == boardY+1):
                        return True
        else:
            print(self.pieceName + self.pieceColor)


