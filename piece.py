import pygame as pg

pg.font.init()

class Piece:
    def __init__(self, pieceName, pieceColor):
        self.pieceName = pieceName
        self.pieceColor = pieceColor
        self.firstMove = False

    def drawPiece(self,X,Y,screen):
        pg.draw.rect(screen, (128,128,128), (X+20, Y+20, 40, 40))
        font=pg.font.SysFont('Comic Sans MS',10)
        text=font.render(self.pieceColor[0]+self.pieceName[0],1,(0,0,0) )
        screen.blit(text,(X+30,Y+30))

    def movePiece(self,board,boardX,boardY,pieceX,pieceY):
        #Moving a peon
        if(self.pieceName == "Peon" ):
            #White
            if(self.pieceColor == "White"):
                #Checking if peon can take
                if(board[boardX][boardY] == 1 and (pieceX == boardX -1 or pieceX == boardX + 1) and pieceY == boardY + 1):
                    if(boardY == 0):
                        self.pieceName = "Queen"
                    return True
                #Moving peon
                if( self.firstMove == 0) : # Checking if its first move of the piece
                    if(pieceX == boardX and (pieceY == boardY + 1 or pieceY == boardY + 2)):
                        #Checking if peon is blocked
                        if(board[boardX][boardY] == 1):
                            return False
                        self.firstMove = 1
                        return True
                else:
                    if(pieceX == boardX and pieceY == boardY + 1):
                        #Checking if peon is blocked
                        if(board[boardX][boardY] == 1):
                            return False
                        if(boardY == 0):
                            self.pieceName = "Queen"
                        return True
            #Black
            if(self.pieceColor == "Black"):
                #Checking if peon can take
                if(board[boardX][boardY] == 1 and (pieceX == boardX -1 or pieceX == boardX + 1) and pieceY == boardY - 1):
                    if(boardY == 7):
                        self.pieceName = "Queen"
                    return True
                #Moving peon
                if( self.firstMove == 0) :
                    if(pieceX == boardX and (pieceY == boardY - 1 or pieceY == boardY - 2)):
                        #Checking if peon is blocked
                        if(board[boardX][boardY] == 1):
                            return False
                        self.firstMove = 1
                        return True
                else:
                    if(pieceX == boardX and pieceY == boardY - 1):
                        #Checking if peon is blocked
                        if(board[boardX][boardY] == 1):
                            return False
                        if(boardY == 7):
                            self.pieceName = "Queen"
                        return True

        #Moving a knight
        if(self.pieceName == "Knight" ):
            print('horse')
            return False

        if(self.pieceName == "Bishop" ):
            print('Preot')
            return False
        
        if(self.pieceName == "Rook" ):
            print('Turn')
            return False

        if(self.pieceName == "Queen" ):
            print('Quuen')
            return False

        if(self.pieceName == "King" ):
            print('Kong')
            return False    


