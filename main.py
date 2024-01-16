import pygame

from Engine import GameState
from Constants import *
import sys



def main():
    global RUNNING, K
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe")
    screen.fill(PEACH)
    font = pygame.font.Font('Cosplay Culture.ttf', 20)

    GS = GameState(screen,SQUARE_WIDTH,SQUARE_HEIGHT,WIDTH,HEIGHT,font)
    GS.DrawGame(BLACK,3)
    GS.LoadImages()


    while RUNNING:
        TURN = GS.cross if (K % 2 == 1) else GS.circle
        TURN_1 = CROSS_1 if (K % 2 == 1) else CIRCLE_1

        MOUSE_POS = pygame.mouse.get_pos()
        (x,y) = int((MOUSE_POS[0] // (WIDTH/3)))  , int((MOUSE_POS[1] // (HEIGHT/3)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

            if event.type == pygame.MOUSEBUTTONDOWN and (x,y) not in MOVE_COUNTER and GS.winner != True:
                MOVE_COUNTER.append((x,y))
                BOARD[y][x] = TURN_1
                GS.WinChecker(BOARD)
                K += 1
                screen.blit(TURN,((x*SQUARE_WIDTH),(y*SQUARE_HEIGHT)))


        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()














