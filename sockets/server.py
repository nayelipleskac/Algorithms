import socket, atexit

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Address Family (AF) - IPv4
#Socket Type- TCP
host = '127.0.0.1' #binds to localhost 127.0.0.1
port = 1234

def handle_exit():
    print('This runs after a keyboard interrupt')
    s.close()
atexit.register(handle_exit)

s.bind((host,port))
print('socket binded to port %s' %(port))
s.listen()
print('Socket is listening...')

while True: 
    conn, addr = s.accept() #get client's socket obj and network address
    print('Got a connecton from ', addr)
    conn.send('thank you for connecting '.encode())
    s.close()
    break
    # data = input('Server: ')
    # conn.sendall(data.encode())
    # data = conn.recv(1024)
    # print(addr,":", data.decode())
    