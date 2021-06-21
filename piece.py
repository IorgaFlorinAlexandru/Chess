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
            if (pieceX == boardX + 1 or pieceX == boardX - 1) and (pieceY == boardY + 2 or pieceY == boardY - 2):
                return True
            if (pieceX == boardX + 2 or pieceX == boardX - 2) and (pieceY == boardY + 1 or pieceY == boardY - 1):
                return True    
            return False

        if(self.pieceName == "Bishop" ):
            copyBoardX = boardX
            copyBoardY = boardY
            print(pieceX)
            print(pieceY)
            print(boardX)
            print(boardY)
            for k in range(0,8):
                print(board[k])
            #Moving diagonally
            #Down right
            while(boardX != -1 and boardY != -1):
                if(pieceX == boardX and pieceY == boardY):
                    return True
                boardX -= 1
                boardY -= 1
            boardX = copyBoardX
            boardY = copyBoardY
            #Up right
            while(boardX != -1 and boardY != 8):
                if(pieceX == boardX and pieceY == boardY):
                    return True
                boardX -= 1
                boardY += 1
            boardX = copyBoardX
            boardY = copyBoardY
            #Up left
            while(boardX != 8 and boardY != -8):
                if(pieceX == boardX and pieceY == boardY):
                    return True
                boardX += 1
                boardY += 1
            boardX = copyBoardX
            boardY = copyBoardY
            #Down left
            while(boardX != 8 and boardY != -1):
                if(pieceX == boardX and pieceY == boardY):
                    return True
                boardX += 1
                boardY -= 1
            return False
        
        if(self.pieceName == "Rook" ):
            copyBoardX = boardX
            copyBoardY = boardY
            #Going right
            while(boardX != -1):
                if( pieceX == boardX and pieceY == boardY):
                    return True
                boardX -= 1
            boardX = copyBoardX
            #Going left
            while(boardX != 8):
                if( pieceX == boardX and pieceY == boardY):
                    return True
                boardX += 1
            boardX = copyBoardX
            #Going up
            while(boardY != 8):
                if( pieceX == boardX and pieceY == boardY):
                    return True
                boardY += 1
            copyBoardY = boardY
            while(boardY != -1):
                if( pieceX == boardX and pieceY == boardY):
                    return True
                boardY -= 1
            copyBoardY = boardY
            return False

        if(self.pieceName == "Queen" ):
            copyBoardX = boardX
            copyBoardY = boardY
            #Moving up,down,right and left
            while(boardX != -1):
                if( pieceX == boardX and pieceY == boardY):
                    return True
                boardX -= 1
            boardX = copyBoardX
            #Going left
            while(boardX != 8):
                if( pieceX == boardX and pieceY == boardY):
                    return True
                boardX += 1
            boardX = copyBoardX
            #Going up
            while(boardY != 8):
                if( pieceX == boardX and pieceY == boardY):
                    return True
                boardY += 1
            boardY = copyBoardY
            while(boardY != -1):
                if( pieceX == boardX and pieceY == boardY):
                    return True
                boardY -= 1
            boardY = copyBoardY
            #Moving diagonally
            #Down right
            while(boardX != -1 and boardY != -1):
                if(pieceX == boardX and pieceY == boardY):
                    return True
                boardX -= 1
                boardY -= 1
            boardX = copyBoardX
            boardY = copyBoardY
            #Up right
            while(boardX != -1 and boardY != 8):
                if(pieceX == boardX and pieceY == boardY):
                    return True
                boardX -= 1
                boardY += 1
            boardX = copyBoardX
            boardY = copyBoardY
            #Up left
            while(boardX != 8 and boardY != -8):
                if(pieceX == boardX and pieceY == boardY):
                    return True
                boardX += 1
                boardY += 1
            boardX = copyBoardX
            boardY = copyBoardY
            #Down left
            while(boardX != 8 and boardY != -1):
                if(pieceX == boardX and pieceY == boardY):
                    return True
                boardX += 1
                boardY -= 1
            return False

        if(self.pieceName == "King" ):
            if( pieceX == boardX or pieceX == boardX - 1 or pieceX == boardX + 1  ) and ( pieceY == boardY or pieceY == boardY - 1 or pieceY == boardY + 1  ):
                return True 
            return False    


