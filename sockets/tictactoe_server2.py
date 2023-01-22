import socket

def run_server():
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    host = socket.gethostname()                           

    port = 9999

    # bind to the port
    serversocket.bind((host, port))                                  

    # queue up to 5 requests
    serversocket.listen(5)                                           

    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()      

        print("Got a connection from %s" % str(addr))
        
        game_board = [" " for i in range(9)]  # Initialize the game board
        current_player = "X"  # X goes first
        game_over = False
        while not game_over:
            # send the current state of the game board to the client
            clientsocket.send(str.encode(" ".join(game_board)))
            # receive the next move from the client
            move = int(clientsocket.recv(1024).decode())
            game_board[move] = current_player
            # check for a win or a draw
            if check_win(game_board, current_player) or " " not in game_board:
                game_over = True
            else:
                # switch to the other player
                current_player = "O" if current_player == "X" else "X"
        
        # send the final state of the game board to the client
        clientsocket.send(str.encode(" ".join(game_board)))
        clientsocket.close()

def check_win(board, player):
    # check rows
    for i in range(0, 9, 3):
        if board[i] == player and board[i+1] == player and board[i+2] == player:
            return True
    # check columns
    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            return True
    # check diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True
    return False

if __name__ == "__main__":
    run_server()
