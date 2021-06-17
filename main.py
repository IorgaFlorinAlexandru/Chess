from piece import Piece
import pygame as pg
import board as board

#Pygame initialization

pg.init()
pg.font.init()
pg.display.set_caption("PyChess")

#Colors

White=(255,255,255)
Black=(0,0,0)

#Screen

screen_size = (800,800)
screen = pg.display.set_mode(screen_size)
screen.fill(White)

#Game Loop

gameBoard = board.Board()
gameBoard.initialiseGame()

def draw_window():
    screen.fill(White)
    gameBoard.drawBoard(screen)

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type==pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            gameBoard.click(pos)

        if event.type == pg.KEYDOWN:
            #Pressing numpad 1 shows all cubes files and ranks
            if event.key == pg.K_KP1:
                 for i in range (0,8):
                    for j in range (0,8):
                        if gameBoard.boardCubes[i][j].showRankAndFile:
                            gameBoard.boardCubes[i][j].showRankAndFile = False
                        else:
                            gameBoard.boardCubes[i][j].showRankAndFile = True
            if event.key == pg.K_KP2:
                for i in range (0,8):
                    for j in range (0,8):
                        gameBoard.boardCubes[i][j].cubePiece = Piece("None","None")
                gameBoard.boardCubes[gameBoard.clickedCubeI][gameBoard.clickedCubeJ].isClicked = False
                gameBoard.clickedCubeI = -1 
                gameBoard.clickedCubeJ = -1
                gameBoard.initialiseGame()

    draw_window()
    pg.display.update()


pg.quit()
    