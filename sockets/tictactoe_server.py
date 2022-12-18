import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w


i= {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

class Server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port= 1234

class Player:
    def __init__(self):
        self.v = None
    def value(self):
        return self.v

class O(Player):
    def __init__(self):
        Player().__init__()

class TicTacToe():
    pass 
    #filling boxes

class Pygame():
    def __init__(self):
        self.pg = pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Tic-Tac-Toe server")
        
    def drawGrid(self):
    #drawing grid
        for x in range(0,600,200):
            for y in range(0,600,200):
                pygame.draw.rect(self.screen,(255,255,255), (x,y,200,200),1)
   
if __name__ == '__main__':

s.bind((host,port))
print('socket binded to port %s' %(port))
s.listen()
print('Socket is listening...')
while True: 
    pygame.display.update()
    # pygame.draw.line(screen, )
    conn, addr = s.accept() 