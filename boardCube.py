import pygame as pg
import piece

pg.init()
pg.font.init()

class boardCube:
    showRankAndFile = False
    isClicked = False
    cubePiece = piece.Piece("None","None")
    
    def __init__(self, cubeSize, cubeFile, cubeRank, cubeX, cubeY, cubeColor):
        self.cubeSize = cubeSize
        self.cubeFile = cubeFile
        self.cubeRank = cubeRank
        self.cubeX = cubeX
        self.cubeY = cubeY
        self.cubeColor = cubeColor
    
    def drawCube(self,screen):
        if self.isClicked:    
            pg.draw.rect(screen, (255,0,0), (self.cubeX, self.cubeY, self.cubeSize, self.cubeSize))
        else:
            pg.draw.rect(screen, self.cubeColor, (self.cubeX, self.cubeY, self.cubeSize, self.cubeSize),)
        if self.showRankAndFile:
            font=pg.font.SysFont('Comic Sans MS',10)
            text=font.render(str(self.cubeFile)+str(self.cubeRank),1,(0,0,0) if self.cubeColor == (255,255,255) else (255,255,255))
            screen.blit(text,(self.cubeX+4,self.cubeY))
        if self.cubePiece.pieceName != "None":
            self.cubePiece.drawPiece(self.cubeX,self.cubeY,screen)

    def checkIfClicked(self, pos):
        if( ( pos[0] >= self.cubeX and pos[0] <= self.cubeX + self.cubeSize ) and ( pos[1] >= self.cubeY and pos[1] <= self.cubeY + self.cubeSize ) ):
            self.isClicked = True
            return True
        else: 
            return False
    def containsPiece(self):
        if self.cubePiece.pieceColor != "None":
            return True
        else:
            return False