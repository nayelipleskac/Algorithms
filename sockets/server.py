import socket, atexit

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Address Family (AF) - IPv4
#Socket Type- TCP
host = '127.0.0.1' #binds to localhost 127.0.0.1
port = 1234

# def handle_exit():
#     print('This runs after a keyboard interrupt')
#     s.close()
# atexit.register(handle_exit)

s.bind((host,port))
print('socket binded to port %s' %(port))
backlog=5 # number of pending connections in queue
s.listen(backlog)
print('Socket is listening...')

# conn.send('thank you for connecting '.encode())

while True: 
    conn, addr = s.accept() #get client's socket obj and network address
    print('Got a connecton from ', addr)
    data = input('Server: ')
    if data == 'break':
        break
    conn.send(data.encode())
    data = conn.recv(1024).decode('utf-8')
    print(addr,":", data.encode())

    s.close()
    