import socket
import atexit
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1' #localhost
port = 1234
s.connect((host, port)) #connect to host and port of server
print('connected')

def handle_exit():
    print('This runs after a keyboard interrupt')
    s.close()
atexit.register(handle_exit)

while True:
    #recieve message from server
    data = s.recv(1024)
    print('recieved from server: ', data.decode())
    #enter message to send
    data = input('say something to the server: ')
    s.send(data.encode())
    if data == 'break':
        break
s.close()
