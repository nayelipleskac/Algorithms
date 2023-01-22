import socket

def run_client():
    # create a socket object
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    host = socket.gethostname()                           

    port = 9999

    # connection to hostname on the port.
    clientsocket.connect((host, port))                               

    game_over = False
