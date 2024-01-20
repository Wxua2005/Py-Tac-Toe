import pygame
from time import sleep
from Engine import GameState
from Constants import *
import sys
import json
pygame.init()
mydict = {
   "TotalGames" : 0,
    "BlueWin" : 0,
    "RedWin" : 0
}
def main():
    global RUNNING, K , P_HOLDER
    screen = pygame.display.set_mode((800, HEIGHT))
    pygame.display.set_caption("TicTacToe")

    font = pygame.font.Font('Cosplay Culture.ttf', 20)
    font2 = pygame.font.Font('Cosplay Culture.ttf', 50)
    font3 = pygame.font.Font('Cosplay Culture.ttf', 30)
    pop_music = pygame.mixer.Sound('pop_sound.mp3')
    restart_music = pygame.mixer.Sound('RestartSound.mp3')
    background_music = pygame.mixer.Sound('Sakura-Girl-Peach-chosic.com_.mp3')

    cursor = pygame.cursors.Cursor((24, 24), (0, 0) ,*pygame.cursors.compile(pygame.cursors.thickarrow_strings))
    wait_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_WAITARROW)
    cross_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_NO)
    pygame.mouse.set_cursor(cursor)

    GS = GameState(screen,SQUARE_WIDTH,SQUARE_HEIGHT,WIDTH,HEIGHT,font)
    background_music.play(loops=4)
    background_music.set_volume(0.1)
    GS.DrawGame(BLACK,3,mydict,font3)
    GS.LoadImages()


    while RUNNING:
        TURN = GS.cross if (K % 2 == 1) else GS.circle
        TURN_1 = CROSS_1 if (K % 2 == 1) else CIRCLE_1
        TURN_2 = 'X' if TURN_1 == CROSS_1 else 'O'

        MOUSE_POS = pygame.mouse.get_pos()
        (x,y) = int((MOUSE_POS[0] // SQUARE_WIDTH))  , int((MOUSE_POS[1] // SQUARE_HEIGHT))

        if x > 2:
            pygame.mouse.set_cursor(cross_cursor)
        else:
            pygame.mouse.set_cursor(cursor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and (x,y) not in GS.MOVE_COUNTER and GS.winner != True and GS.winner2 != True and 0 <= x <= 2:
                GS.MOVE_COUNTER.append((x,y))
                GS.board[y][x] = TURN_1
                GS.board2[y][x] = TURN_2
                GS.WinChecker(GS.board,mydict)
                K += 1
                pop_music.play()
                screen.blit(TURN,((x*SQUARE_WIDTH),(y*SQUARE_HEIGHT)))


            if event.type == pygame.MOUSEBUTTONDOWN and GS.End == True:
                restart_rect = pygame.Rect((168, 289), (156, 138))
                if restart_rect.collidepoint(pygame.mouse.get_pos()):
                    mydict["TotalGames"] += 1
                    pygame.quit()
                    return 1
                else:
                    sleep(1.25)
                    return None

            if event.type == pygame.KEYDOWN:               # Restart and Undo Keys (R and U keys)
                if event.key == pygame.K_r:                # Undo needs to be fixes (Engine.py)
                    GS.Reset()
                elif event.key == pygame.K_u:
                    pass


        if GS.winner == True:
            pygame.mouse.set_cursor(wait_cursor)
            GS.EndScreen(GS,font2,restart_music)
            pygame.mouse.set_cursor(cursor)


        pygame.display.update()



if __name__ == "__main__":
    k = main()
    if k == None:
        sys.exit()
    while k == 1:
        pygame.init()
        k = main()

