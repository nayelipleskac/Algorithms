import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1' #localhost
port = 1234

s.connect((host, port)) #connect to host and port of server
print('connected')

data = s.recv(1024)
print(data)
s.close()
# print(data.decode())
# data = input('Client: ')
# s.sendall(data.encode())