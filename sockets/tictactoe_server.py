import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w
from pygame.locals import *
from threading import Thread


# class Player:
#     def __init__(self):
#         self.v = None
#     def value(self):
#         return self.v

# class X(Player):
#     def __init__(self):
#         Player().__init__()
#         self.v = 'x'

# class O(Player):
#     def __init__(self):
#         super().__init__()
#         print(super())
#         self.v = 'o'


def create_thread(target):
    t = Thread(target=target) #argument - target function
    t.daemon = True
    t.start() 

class Server(socket.socket):
    def __init__(self, host = 'localhost', port = 1234):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port= port
        self.screen = None
        self.board= {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

        self.p = 'x'
        self.running = True
        self.conn = None
        self.pos = None
        self.turn = False

        self.bind((self.host, self.port))
        self.listen(5)

    def showtext(self,msg,x,y):
        font= pygame.font.SysFont("freesans" ,32)
        msgobj = font.render(msg,False,(255,0,0))
        self.screen.blit(msgobj,(x,y))

    def start(self):
        self.conn, addr = self.accept()  #accept connection 
        print('Got a connecton from ', addr)
        self.turn = True #server's turn now
        
        self.play()
        print('Got a connecton from ', addr)
        self.conn.send('thank you for connecting '.encode())
    def play(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Tic-Tac-Toe server")
        for x in range(0,600,200):
            for y in range(0,600,200):
                pygame.draw.rect(self.screen,(255,255,255), (x,y,200,200),1)
        # btn_rect = pygame.Rect(0,600-50,100,50)
        # font = pygame.font.Font(None,36)
        # btn_label = font.render('Close Server', True, (255,255,255))
        # pygame.draw.rect(self.screen,(0,128,255), btn_rect )
        # self.screen.blit(btn_label, btn_rect.center)
        
        print('server: set up game board')
        print('SERVER STARTS FIRST')
        while self.running:
            create_thread(self.accept_message)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and self.turn ==True:
                    self.pos = event.pos
                    create_thread(self.send_message)

            # print('server turn is:', self.turn)
    def accept_message(self):
        while True:
            data = self.conn.recv(1024).decode()
            if not data:
                break
            print('Received', data)
            x,y = data.split(',',1)
            self.drawO(int(x),int(y))
            self.boxes(int(x),int(y),'o')
            self.turn = True
            self.winner()
    def send_message(self):
        x,y= self.pos
        print('x: {}, y: {}'.format(x,y))
        self.conn.send('{}, {}'.format(x,y).encode())
        self.drawX(x,y)
        self.boxes(x,y,'x')
        print('drawing O in erver')
        self.turn = False   
        print('server just played, client\'s turn')  
        self.winner()                 
       
    def drawX(self,x,y):  
        pygame.draw.line(self.screen,(255,255,255),(x-50,y-50),(x+50,y+50),1) 
        pygame.draw.line(self.screen,(255,255,255),(x+50,y-50),(x-50,y+50),1)
    def drawO(self,x,y):
        pygame.draw.circle(self.screen,(255,255,255),(x,y),70,1) 
    def boxes(self, x, y, player):
        if x in range(0,200) and y in range(0,200): #box 1
            self.update_board(1, player)
        elif x in range(200,400) and y in range(0,200): #box 2
            self.update_board(2, player)
        elif x in range(400,600) and y in range(0,200): #box 3
            self.update_board(3, player)
        elif x in range(0,200) and y in range(200,400): #box 4
            self.update_board(4,player)
        elif x in range(200,400) and y in range(200,400): #box 5
            self.update_board(5, player)
        elif x in range(400,600) and y in range(200,400): #box 6
            self.update_board(6, player)
        elif x in range(0,200) and y in range(400,600): #box 7
            self.update_board(7, player)
        elif x in range(200,400) and y in range(400,600): #box 8
            self.update_board(8, player)
        elif x in range(400,600) and y in range(400,600): #box 9
            self.update_board(9, player)
    def winner(self):
        # if len(self.board.values()) >= 3:
        if self.board[1]=='x' and self.board[2]== 'x' and self.board[3] == 'x':
            self.printWinner('x')
        elif self.board[1]=='o' and self.board[2]== 'o' and self.board[3] == 'o':
            self.printWinner('o')
        elif self.board[4]=='x' and self.board[5]== 'x' and self.board[6] == 'x':
            self.printWinner('x')
        elif self.board[4]=='o' and self.board[5]== 'o' and self.board[6] == 'o':
            self.printWinner('o')
        elif self.board[7]=='x' and self.board[8]== 'x' and self.board[9] == 'x':
            self.printWinner('x')
        elif self.board[7]=='o' and self.board[8]== 'o' and self.board[9] == 'o':
            self.printWinner('o')
        elif self.board[1]=='x' and self.board[5]== 'x' and self.board[9] == 'x':
            self.printWinner('x')
        elif self.board[1]=='o' and self.board[5]== 'o' and self.board[9] == 'o':
            self.printWinner('o')
        elif self.board[7]=='x' and self.board[5]=='x' and self.board[3] == 'x':
            self.printWinner('x')
        elif self.board[7]=='o' and self.board[5]=='o' and self.board[3] == 'o':
            self.printWinner('o')
        elif self.board[2]== 'x' and self.board[5]== 'x' and self.board[8] == 'x':
            self.printWinner('x')
        elif self.board[2]== 'o' and self.board[5]== 'o' and self.board[8] == 'o':
            self.printWinner('o')
        elif self.board[1]=='x' and self.board[4]== 'x' and self.board[7] == 'x':
            self.printWinner('x')
        elif self.board[1]=='o' and self.board[4]== 'o' and self.board[7] == 'o':
            self.printWinner('o')
        elif self.board[3]=='x' and self.board[6]=='x' and self.board[9] == 'x':
            self.printWinner('x')
        elif self.board[3]=='o' and self.board[6]=='o' and self.board[9] == 'o':
            self.printWinner('o')
        elif (' ' not in self.board.values()):
            print('tie!')
    def update_board(self,pos, val):
        # def update(self, pos, val):
        self.board[pos] = val
        print('server: ', self.board)

    def printWinner(self,indicator):
        print('PLAYER {} WINS'.format(indicator))
        self.showtext('PLAYER {} WINS'.format(indicator), 200,20)
        pygame.display.update()
        
   
if __name__ == '__main__':
    # player = X() #server is X
    server = Server('127.0.0.1', 1234)
    server.start()


