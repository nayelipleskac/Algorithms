import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w
from pygame.locals import *

class Player:
    def __init__(self):
        self.v = None
    def value(self):
        return self.v

class O(Player):
    def __init__(self):
        Player().__init__()
        self.v = 'o'

class X(Player):
    def __init__(self):
        super().__init__()
        self.v = 'x'

class TicTacToe():
    def __init__(self): 
        self.board= {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        self.p1 = O()
    def update(self, pos, val):
        self.board[pos] = val
        
##########################################
#client starts: 
# connect clinet 
# mark board
# open connection to send server (pos, val)
# close connection
# wait for server data
# update the board
# repeat 
##########################################
class Client():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1' #localhost
        self.port = 1234
        self.screen = None

    def startGame(self):
        print('Starting game...')
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Tic-Tac-Toe client")
        #creating the board on screen
        for x in range(0,600,200):
            for y in range(0,600,200):
                pygame.draw.rect(self.screen,(255,255,255), (x,y,200,200),1)

        self.s.connect((self.host, self.port)) #reopening socket for new thread
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x,y= pygame.mouse.get_pos()
                    print(x,y)
                    #draw X in box 1
                    if x in range(0,200) and y in range(0,200):
                        pygame.draw.line(self.screen,(255,255,255),(x-50,y-50),(x+50,y+50),1) 
                        pygame.draw.line(self.screen,(255,255,255),(x+50,y-50),(x-50,y+50),1)
                    #sending x,y message to server 
                    print('Client: connected')
                    data = self.s.recv(1024)
                    print(data.decode())
                    data = str(x) + ','+ str(y).encode()
                    self.s.sendall(data.encode())  
                    self.s.close()  
                    #keep connection open 
            pygame.display.update()
       
    def start(self):
        
        self.s.connect((self.host, self.port)) #connect to host and port of server
        print('Client: connected')
        #recieve data from server
        data = self.s.recv(1024)
        print('Client: ', data)
        self.s.close()
        self.startGame()

if __name__ == '__main__':
    client = Client()
    client.start()
    # game.drawGrid()


