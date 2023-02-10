import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w
from pygame.locals import *

class Player:
    def __init__(self):
        self.v = None
    def value(self):
        return self.v

class X(Player):
    def __init__(self):
        Player().__init__()
        self.v = 'x'

class O(Player):
    def __init__(self):
        super().__init__()
        print(super())
        self.v = 'o'

class TicTacToe():
    def __init__(self): 
        self.board= {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        self.p2 = O()
    def update(self, pos, val):
        self.board[pos] = val

class Server():
    def __init__(self):
        self.host = '127.0.0.1'
        self.port= 1234
        self.backlog = 5
        self.screen = None
    def startGame(self):
        print('Starting game...')
        pygame.init()  #initiate pygame and set caption
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Tic-Tac-Toe server")
        for x in range(0,600,200):
            for y in range(0,600,200):
                pygame.draw.rect(self.screen,(255,255,255), (x,y,200,200),1)
        print('Server: set up board')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host,self.port))
            print('socket binded to port %s' %(self.port))
            s.listen(self.backlog)
            conn, addr = s.accept() #get client's socket obj and network address
            print('Socket is listening...')
            print('Got a connecton from ', addr)
            with conn:
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                            x,y = pygame.mouse.get_pos()
                            data = str(x) + ',' + str(y)
                            print('Server: mouse btn position: ', data)
                            conn.send(data.encode())
                            data = conn.recv(1024).decode('utf-8')
                            print(addr,":", data.encode())
                            print('Server: Message recieved: ', data)

                            y=data.split(',')
                            print('Server split data', y)
                            #drawing O in box 1
                            # if x in range(0,200) and y in range(0,200):
                            #     self.drawX(x,y,self.screen)
                            #     print('Server in box 1')
                            # if x in range(200,400) and y in range(0,200):
                            #     self.drawX(x,y,self.screen)
                            #     print('Server in box 2')
                            # if x in range(400,600) and y in range(0,200):
                            #     self.drawX(x,y,self.screen)
                            #     print('Server in box 3')
                            # if x in range(0,200) and y in range(200,400):
                            #     self.drawX(x,y,self.screen)
                            #     print('Server in box 4')
                            # if x in range(200,400) and y in range(200,400):
                            #     self.drawX(x,y,self.screen)
                            #     print('Server in box 5')
                            # if x in range(400,600) and y in range(200,400):
                            #     self.drawX(x,y,self.screen)
                            #     print('Server in box 6')
                            # if x in range(0,200) and y in range(400,600):
                            #     self.drawX(x,y,self.screen)
                            #     print('Server in box 7')
                            # if x in range(200,400) and y in range(400,600):
                            #     self.drawX(x,y,self.screen)
                            #     print('Server in box 8')
                            # if x in range(400,600) and y in range(400,600):
                            #     self.drawX(x,y,self.screen)
                            #     print('Server in box 9')
                            
                            #sending x,y position message to client
                            # data = (str(event.pos[0]) + "," + str(event.pos[1])).encode()
                           
                    pygame.display.update()
    
    def drawX(self,x,y, screen):  
        pygame.draw.line(screen,(255,255,255),(x-50,y-50),(x+50,y+50),1) 
        pygame.draw.line(screen,(255,255,255),(x+50,y-50),(x-50,y+50),1)

    def start(self):
        self.s.bind((self.host, self.port)) #start server connection 
        print('socket binded to port %s' %(self.port))
        print('Socket is listening...')
        self.s.listen()
        conn, addr = self.s.accept()  #accept connection 
        print('Got a connecton from ', addr)
        conn.send('thank you for connecting '.encode())
        self.s.close()
        self.startGame()
   
if __name__ == '__main__':
    player = X() #server is X
    server = Server()
    server.startGame()


