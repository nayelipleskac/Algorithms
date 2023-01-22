import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w

i= {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

class Server():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port= 1234
    def connectServer(self):
        self.s.bind((self.host, self.port))
        print('socket binded to port %s' %(self.port))
        self.s.listen()
        print('Socket is listening...')
        while True: 
            # pygame.display.update()
            # pygame.draw.line(screen, )
            conn, addr = self.s.accept() 
            print('Got a connecton from ', addr)
            conn.send('thank you for connecting '.encode())
            self.s.close()
            
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
    #filling boxes logic

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
        pygame.display.update()
    def run(self):
        pass
   
if __name__ == '__main__':
    game = Pygame()
    player = O()
    server = Server()
    server.connectServer()
    # game.drawGrid()
    # server.connectServer()

