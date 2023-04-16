import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w
from pygame.locals import *
from threading import Thread

################################ 
# fix og code to make cood. send


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
# not used 
class MyThread(Thread):
    def __init__(self, x, y, socket):
        Thread.__init__(self)
        self.socket = socket
        self.x = x
        self.y = y
    def send_points(self):
        # data = (str(self.x), ',', str(self.y))
        data =('client: ','x: {}, y: {}'.format(self.x,self.y)) 
        self.socket.send(data.encode())
    def run(self):
        self.send_points()


def create_thread(target):
    t = Thread(target=target) #argument - target function
    t.daemon = True
    t.start()        
class Client(socket.socket):
    def __init__(self, host = socket.gethostname(), port = 1234):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host #localhost
        self.port = port
        self.screen = None
        self.player = 'o'
        self.na = socket.gethostname()
        self.board= {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        self.running = True

    def accept_message(self):
        while True:
            data = self.recv(1024).decode()
            if not data:
                break
            print('Received', data)

    def start(self):
        self.connect((self.host, self.port))
        self.sendall('Client: connection established'.encode())
        print('Client: Connected to {}'.format(self.host, self.na))
        self.play()
    def play(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        pygame.display.set_caption("Tic-Tac-Toe client")
        for x in range(0,600,200):
            for y in range(0,600,200):
                pygame.draw.rect(self.screen,(255,255,255), (x,y,200,200),1)
        print('client: set up game board')
        while self.running:
            create_thread(self.accept_message)
            pygame.display.update()
            # data = self.s.recv(1024).decode()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                    x,y = event.pos
                    print('x:{}, y:{}'.format(x,y))
                    self.sendall('{},{}'.format(x,y).encode())
                        
                
    def drawO(self,x,y,screen):
        pygame.draw.circle(screen,(255,255,255),(x,y),70,1) #o 
   


if __name__ == '__main__':   
    client = Client('127.0.0.1', 1234)
    client.start()


