import pygame

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
        self.winner = None
        self.winner2 = None
        self.score = 0
        self.End = None
        self.board = [[0,0,0],
                     [0,0,0],
                     [0,0,0]]
        self.MOVE_COUNTER = []
    def DrawGame(self,COLOR,THICKNESS):
        for i in range(1, 3):
            pygame.draw.line(self.screen, COLOR, (i * self.SQUARE_WIDTH, 0), (i * self.SQUARE_WIDTH, self.HEIGHT), width=THICKNESS)
            pygame.draw.line(self.screen, COLOR, (0, i * self.SQUARE_HEIGHT), (self.WIDTH, i * self.SQUARE_HEIGHT), width=THICKNESS)

        for i in range(0,3):
            for j in range(0,3):
                self.screen.blit(self.font.render(f'({j},{i})',True,COLOR),(j*self.SQUARE_WIDTH,i*self.SQUARE_HEIGHT))

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

    def WinChecker(self,board):
        for rows in board:

            if sum(rows) == 3:
                print('Winner Red')
                self.winner = True
                self.winner2 = True

            elif sum(rows) == -3:
                print('Winner Blue')
                self.winner =  True
                self.winner2 = True

        for i in range(0, 3):
            for j in range(0, 3):
                self.score += board[j][i]

                if self.score == 3:
                    print('Winner Red')
                    self.winner =  True
                    self.winner2 = True

                elif self.score == -3:
                    print('Winner Blue')
                    self.winner =  True
                    self.winner2 = True

            self.score = 0

        if board[0][0] + board[1][1] + board[2][2] == 3 or board[2][0] + board[1][1] + board[0][2] == 3:
            print('Winner Red')
            self.winner = True
            self.winner2 = True

        elif board[0][0] + board[1][1] + board[2][2] == -3 or board[2][0] + board[1][1] + board[0][2] == -3:
            print('Winner Blue')
            self.winner = True
            self.winner2 = True

        if self.winner == None and len(self.MOVE_COUNTER) == 9:
            print('Draw')



