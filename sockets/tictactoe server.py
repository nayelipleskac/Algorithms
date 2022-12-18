import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w

pygame.init()
pygame.display.set_caption("Tic-Tac-Toe")
screen = pygame.display.set_mode((600, 600))

x_img = pygame.load('x_img.png')
o_img = pygame.load('o_img.png')
x_img = pygame.transform.scale(x_img, (80,80))
o_img = pygame.transform.scale(o_img, (80,80))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port= 1234

s.bind((host, port))
s.bind((host,port))
print('socket binded to port %s' %(port))
s.listen()
print('Socket is listening...')
while True: 
    pygame.display.update()
    pygame.draw.line(screen, )
    conn, addr = s.accept() 