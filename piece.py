import pygame as pg

pg.font.init()

class Piece:
    def __init__(self, pieceName, pieceColor):
        self.pieceName = pieceName
        self.pieceColor = pieceColor
        self.firstMove = False

    def drawPiece(self,X,Y,screen):
        #Drawing Peons
        if(self.pieceName == "Peon"):
            if(self.pieceColor == "White"):
                pieceImg = pg.image.load("PieceIcons/wp.png")
                screen.blit(pieceImg,(X+7,Y+7))
            else:
                pieceImg = pg.image.load("PieceIcons/bp.png")
                screen.blit(pieceImg,(X+7,Y+7))
        #Drawing Knights
        if(self.pieceName == "Knight"):
            if(self.pieceColor == "White"):
                pieceImg = pg.image.load("PieceIcons/wN.png")
                screen.blit(pieceImg,(X+8,Y+10))
            else:
                pieceImg = pg.image.load("PieceIcons/bN.png")
                screen.blit(pieceImg,(X+8,Y+10))
        #Drawing Bishops
        if(self.pieceName == "Bishop"):
            if(self.pieceColor == "White"):
                pieceImg = pg.image.load("PieceIcons/wB.png")
                screen.blit(pieceImg,(X+8,Y+10))
            else:
                pieceImg = pg.image.load("PieceIcons/bB.png")
                screen.blit(pieceImg,(X+8,Y+10))
        #Drawing Rooks
        if(self.pieceName == "Rook"):
            if(self.pieceColor == "White"):
                pieceImg = pg.image.load("PieceIcons/wR.png")
                screen.blit(pieceImg,(X+8,Y+10))
            else:
                pieceImg = pg.image.load("PieceIcons/bR.png")
                screen.blit(pieceImg,(X+8,Y+10))
        #Drawing Queens
        if(self.pieceName == "Queen"):
            if(self.pieceColor == "White"):
                pieceImg = pg.image.load("PieceIcons/wQ.png")
                screen.blit(pieceImg,(X+8,Y+10))
            else:
                pieceImg = pg.image.load("PieceIcons/bQ.png")
                screen.blit(pieceImg,(X+8,Y+10))
        #Drawing Kings
        if(self.pieceName == "King"):
            if(self.pieceColor == "White"):
                pieceImg = pg.image.load("PieceIcons/wK.png")
                screen.blit(pieceImg,(X+10,Y+7))
            else:
                pieceImg = pg.image.load("PieceIcons/bK.png")
                screen.blit(pieceImg,(X+10,Y+7))

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
            howMany = 0
            #Moving diagonally
            #Down right
            while(boardX != -1 and boardY != -1):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if(pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    print(howMany)
                    return True
                boardX -= 1
                boardY -= 1
            boardX = copyBoardX
            boardY = copyBoardY
            howMany = 0
            #Up right
            while(boardX != -1 and boardY != 8):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if(pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    print(howMany)
                    return True
                boardX -= 1
                boardY += 1
            boardX = copyBoardX
            boardY = copyBoardY
            howMany = 0
            #Up left
            while(boardX != 8 and boardY != 8):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if(pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    print(howMany)
                    return True
                boardX += 1
                boardY += 1
            boardX = copyBoardX
            boardY = copyBoardY
            howMany = 0
            #Down left
            while(boardX != 8 and boardY != -1):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if(pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    print(howMany)
                    return True
                boardX += 1
                boardY -= 1
            return False
        
        if(self.pieceName == "Rook" ):
            copyBoardX = boardX
            copyBoardY = boardY
            howMany = 0
            #Going right
            while(boardX != -1):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if( pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardX -= 1
            boardX = copyBoardX
            howMany = 0
            #Going left
            while(boardX != 8):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if( pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardX += 1
            boardX = copyBoardX
            howMany = 0
            #Going up
            while(boardY != 8):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if( pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardY += 1
            boardY = copyBoardY
            howMany = 0
            #Going down
            while(boardY != -1):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if( pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardY -= 1
            return False

        if(self.pieceName == "Queen" ):
            copyBoardX = boardX
            copyBoardY = boardY
            howMany = 0
            #Moving up,down,right and left
            while(boardX != -1):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if( pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardX -= 1
            boardX = copyBoardX
            howMany = 0
            #Going left
            while(boardX != 8):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if( pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardX += 1
            boardX = copyBoardX
            howMany = 0
            #Going up
            while(boardY != 8):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if( pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardY += 1
            boardY = copyBoardY
            howMany = 0
            #Going up
            while(boardY != -1):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if( pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardY -= 1
            boardY = copyBoardY
            howMany = 0
            #Moving diagonally
            #Down right
            while(boardX != -1 and boardY != -1):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if(pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardX -= 1
                boardY -= 1
            boardX = copyBoardX
            boardY = copyBoardY
            howMany = 0
            #Up right
            while(boardX != -1 and boardY != 8):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if(pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardX -= 1
                boardY += 1
            boardX = copyBoardX
            boardY = copyBoardY
            howMany = 0
            #Up left
            while(boardX != 8 and boardY != 8):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if(pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardX += 1
                boardY += 1
            boardX = copyBoardX
            boardY = copyBoardY
            howMany = 0
            #Down left
            while(boardX != 8 and boardY != -1):
                if(board[boardX][boardY] == 1):
                    howMany += 1
                if(pieceX == boardX and pieceY == boardY):
                    if(howMany - board[copyBoardX][copyBoardY] >= 2):
                        return False
                    return True
                boardX += 1
                boardY -= 1
            return False

        if(self.pieceName == "King" ):
            if( pieceX == boardX or pieceX == boardX - 1 or pieceX == boardX + 1  ) and ( pieceY == boardY or pieceY == boardY - 1 or pieceY == boardY + 1  ):
                return True 
            return False    


