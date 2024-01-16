import pygame
from time import sleep
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
    font2 = pygame.font.Font('Cosplay Culture.ttf', 50)

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

        if GS.winner == True:
            pygame.display.update()
            sleep(2)
            screen.fill('Pink')
            GS.winner = False
            z = BOARD[MOVE_COUNTER[-1][1]][MOVE_COUNTER[-1][0]]
            screen.blit(font2.render(f'Game Over',True,'Maroon'),(130,50))
            screen.blit(font2.render(f'{PIECE_WINNER[z]} WINS', True, 'Purple'), (130, 130))
            screen.blit(GS.restart,(190,300))
            pygame.draw.lines(screen,BLACK,False,[(168,289),(324,289),(324,427),(168,427),(168,289)])
            restart_rect = pygame.Rect((168,289),(156,138))
            if restart_rect.collidepoint(pygame.mouse.get_pos()):
                print('yes')

        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()













