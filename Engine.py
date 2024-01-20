import pygame
from time import sleep
class GameState:
    def __init__(self,screen,SQUARE_WIDTH,SQUARE_HEIGHT,WIDTH,HEIGHT,font):
        self.screen = screen
        self.SQUARE_WIDTH = SQUARE_WIDTH
        self.SQUARE_HEIGHT = SQUARE_HEIGHT
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.font = font
        self.cross = None
        self.circle = None
        self.icon = None
        self.winner = None
        self.winner2 = None
        self.score = 0
        self.End = None
        self.board = [[0,0,0],
                     [0,0,0],
                     [0,0,0]]
        self.board2 = [['--','--','--'],
                      ['--','--','--'],
                      ['--','--','--']]
        self.MOVE_COUNTER = []
        self.PIECE_WINNER = {1 : 'CROSS',
                            -1 : 'CIRCLE'}
        self.PEACH = (255, 229, 180)
        self.BROWN = (196, 164, 132)
        self.o = {'X': self.cross,
                  'O': self.circle,
                  '--': self.icon}
        self.GAME_SCREEN = pygame.Rect((0, 0), (self.WIDTH, self.HEIGHT))
        self.SIDE_BAR = pygame.Rect((self.WIDTH,0),(300,self.HEIGHT))

    def DrawGame(self,COLOR,THICKNESS,mydict,font):
        self.screen.fill(self.PEACH, self.GAME_SCREEN)
        self.screen.fill(self.BROWN, self.SIDE_BAR)

        for i in range(1, 3):
            pygame.draw.line(self.screen, COLOR, (i * self.SQUARE_WIDTH, 0), (i * self.SQUARE_WIDTH, self.HEIGHT), width=THICKNESS)
            pygame.draw.line(self.screen, COLOR, (0, i * self.SQUARE_HEIGHT), (self.WIDTH, i * self.SQUARE_HEIGHT), width=THICKNESS)

        for i in range(0,3):
            for j in range(0,3):
                self.screen.blit(self.font.render(f'({j},{i})',True,COLOR),(j*self.SQUARE_WIDTH,i*self.SQUARE_HEIGHT))

        self.screen.blit(font.render(f'Game Count : {mydict["TotalGames"]}',True,'LightGreen'),(550,10))
        self.screen.blit(font.render(f'Red Win: {mydict["RedWin"]}', True, (255, 71, 76)), (550, 60))
        self.screen.blit(font.render(f'Blue Win : {mydict["BlueWin"]}', True, (173, 216, 230)), (550, 110))
        pygame.draw.line(self.screen,COLOR,(500,0),(500,self.HEIGHT),width=3)
    def LoadImages(self):
        self.icon = pygame.image.load('iconimg.png').convert()
        self.cross = pygame.image.load('cross.png').convert_alpha()
        self.circle = pygame.image.load('circle.png').convert_alpha()
        self.restart = pygame.image.load('restart.png').convert_alpha()
        self.cross = pygame.transform.scale(self.cross, (150, 150))
        self.circle = pygame.transform.scale(self.circle, (170, 170))
        self.restart = pygame.transform.scale(self.restart,(120,120))
        self.cross.set_colorkey((255, 255, 255))
        self.circle.set_colorkey((255, 255, 255))

    def WinChecker(self,board,mydict):
        for rows in board:

            if sum(rows) == 3:
                print('Winner Red')
                mydict["RedWin"] += 1
                self.winner = True
                self.winner2 = True

            elif sum(rows) == -3:
                print('Winner Blue')
                mydict["BlueWin"] += 1
                self.winner =  True
                self.winner2 = True

        for i in range(0, 3):
            for j in range(0, 3):
                self.score += board[j][i]

                if self.score == 3:
                    print('Winner Red')
                    mydict["RedWin"] += 1
                    self.winner =  True
                    self.winner2 = True

                elif self.score == -3:
                    print('Winner Blue')
                    mydict["BlueWin"] += 1
                    self.winner =  True
                    self.winner2 = True

            self.score = 0

        if board[0][0] + board[1][1] + board[2][2] == 3 or board[2][0] + board[1][1] + board[0][2] == 3:
            print('Winner Red')
            mydict["RedWin"] += 1
            self.winner = True
            self.winner2 = True

        elif board[0][0] + board[1][1] + board[2][2] == -3 or board[2][0] + board[1][1] + board[0][2] == -3:
            print('Winner Blue')
            mydict["BlueWin"] += 1
            self.winner = True
            self.winner2 = True

        if self.winner == None and len(self.MOVE_COUNTER) == 9:
            print('Draw')

    def EndScreen(self,GS,font2,music):
        pygame.display.update()
        sleep(2)
        self.screen.fill('Pink',self.GAME_SCREEN)
        GS.winner = False
        LAST_MOVE = GS.board[GS.MOVE_COUNTER[-1][1]][GS.MOVE_COUNTER[-1][0]]
        self.screen.blit(font2.render(f'Game Over', True, 'Maroon'), (130, 50))
        self.screen.blit(font2.render(f'{GS.PIECE_WINNER[LAST_MOVE]} WINS', True, 'Purple'), (130, 130))
        self.screen.blit(GS.restart, (190, 300))
        pygame.draw.lines(self.screen, 'BLACK', False, [(168, 289), (324, 289), (324, 427), (168, 427), (168, 289)], width=4)
        music.play()
        GS.End = True

    def Reset(self):
        self.board = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        self.MOVE_COUNTER = []
        self.DrawGame((0,0,0), 3)

    def Undo(self,x,y):
        self.board2[self.MOVE_COUNTER[-1][1]][self.MOVE_COUNTER[-1][0]] = "--"
        self.board[self.MOVE_COUNTER[-1][1]][self.MOVE_COUNTER[-1][0]] = 0
        self.screen.fill(self.PEACH)

        for row in range(0,3):
            for col in (0,3):
                ik = self.o[self.board2[row][col]]
                print(ik)
                self.screen.blit(ik,((x*self.SQUARE_WIDTH),(y*self.SQUARE_HEIGHT)))

