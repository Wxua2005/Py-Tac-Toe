import pygame
from time import sleep
from Engine import GameState
from Constants import *
import sys

def main():
    global RUNNING, K , P_HOLDER
    pygame.init()
    GAME_SCREEN = pygame.Rect((0,0),(500,HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TicTacToe")
    screen.fill(PEACH)
    font = pygame.font.Font('Cosplay Culture.ttf', 20)
    font2 = pygame.font.Font('Cosplay Culture.ttf', 50)
    pop_music = pygame.mixer.Sound('pop_sound.mp3')
    restart_music = pygame.mixer.Sound('RestartSound.mp3')
    bitmap_2 = pygame.cursors.Cursor(
        (24, 24), (0, 0) ,*pygame.cursors.compile(pygame.cursors.thickarrow_strings)
    )
    pygame.mouse.set_cursor(bitmap_2)

    GS = GameState(screen,SQUARE_WIDTH,SQUARE_HEIGHT,WIDTH,HEIGHT,font)
    GS.DrawGame(BLACK,3)
    GS.LoadImages()


    while RUNNING:
        TURN = GS.cross if (K % 2 == 1) else GS.circle
        TURN_1 = CROSS_1 if (K % 2 == 1) else CIRCLE_1

        MOUSE_POS = pygame.mouse.get_pos()
        (x,y) = int((MOUSE_POS[0] // SQUARE_WIDTH))  , int((MOUSE_POS[1] // SQUARE_HEIGHT))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and (x,y) not in GS.MOVE_COUNTER and GS.winner != True and GS.winner2 != True:
                GS.MOVE_COUNTER.append((x,y))
                GS.board[y][x] = TURN_1
                GS.WinChecker(GS.board)
                K += 1
                pop_music.play()
                screen.blit(TURN,((x*SQUARE_WIDTH),(y*SQUARE_HEIGHT)))

            if event.type == pygame.MOUSEBUTTONDOWN and GS.End == True:
                restart_rect = pygame.Rect((168, 289), (156, 138))
                if restart_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    return 1
                else:
                    sleep(1.25)
                    return None


        if GS.winner == True:
            pygame.display.update()
            sleep(2)
            screen.fill('Pink')
            GS.winner = False
            z = GS.board[GS.MOVE_COUNTER[-1][1]][GS.MOVE_COUNTER[-1][0]]
            screen.blit(font2.render(f'Game Over',True,'Maroon'),(130,50))
            screen.blit(font2.render(f'{PIECE_WINNER[z]} WINS', True, 'Purple'), (130, 130))
            screen.blit(GS.restart,(190,300))
            pygame.draw.lines(screen,BLACK,False,[(168,289),(324,289),(324,427),(168,427),(168,289)],width=3)
            restart_music.play()
            GS.End = True

        


        pygame.display.update()



if __name__ == "__main__":
    k = main()
    if k == None:
        sys.exit()
    while k == 1:
        k = main()
