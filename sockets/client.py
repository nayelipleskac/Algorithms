import socket

host = 'localhost'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port)) #connect to host and port of server
print('connected')

while True: 
    data = s.recv(1024)
    print(data.decode())
    data = input('Client: ')
    s.sendall(data.encode())