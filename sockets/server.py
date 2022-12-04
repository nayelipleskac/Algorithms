import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Address Family (AF) - IPv4
#Socket Type- TCP
host = '127.0.0.1' #binds to localhost 127.0.0.1
port = 12345

s.bind((host,port))
s.listen()
print('Socket is listening')
conn, addr = s.accept() #get client's socket obj and network address

with conn:
    print('Got a connecton from ', addr)
    while True: 
        data = input('Server: ')
        conn.sendall(data.encode())
        data = conn.recv(1024)
        print(addr,":", data.decode())