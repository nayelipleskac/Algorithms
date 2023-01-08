import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w


class Player:
    def __init__(self):
        self.v = None #value
    def value(self):
        return self.v

class Client():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1' #localhost
        self.port = 1234
    def x(self):
        while True:
            pygame.display.update()
            data = self.s.recv(1024)
            print(data)
            self.s.close()
            
    def connectClient(self):
        self.s.connect((self.host, self.port)) #connect to host and port of server
        print('connected')

class Pygame():
    def __init__(self):
        # self.pg = pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        
    def drawGrid(self):
        pygame.init()
        pygame.display.set_caption("Tic-Tac-Toe client")
        for x in range(0,600,200):
            for y in range(0,600,200):
                pygame.draw.rect(self.screen,(255,255,255), (x,y,200,200),1)
        pygame.display.update()
    def run():
        pass

class X(Player):
    def __init__(self):
        super().__init__()
        print(super())


if __name__ == '__main__':
    client = Client()
    game = Pygame()
    game.drawGrid()


