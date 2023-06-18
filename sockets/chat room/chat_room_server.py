#Server
#socket imports
import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w
from pygame.locals import *
from threading import Thread

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import random, time

#multithreading imports
import threading, time, random, string
from threading import Thread, active_count, current_thread
from datetime import datetime

connections = {} #keys as username and value as client's socket obj

def create_thread(target):
    t= Thread(target=target)
    t.daemon = True
    t.start()

class ChatRoom(socket.socket):
    def __init__(self, host = 'localhost', port = 1234):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.conn = None
        self.bind((self.host, self.port))
        self.listen(4)
    def start(self): #continuously accepts new conn
        while True: 
            self.conn, addr = self.accept()  
            print('Got a connection from ', addr)
            self.accept_message()
            
    def accept_message(self): 
        while True: 
            username = self.conn.recv(1024).decode('utf-8') #recv username from server
            print('Received from client: ', username)
            connections[username] = self.conn
            print('DICTIONARY: ',connections)
            #using connections dictionary, add username and socket obj? 
            #key value pair 
            self.listener(username, self.conn)
    def send_everyone(self, message):
        for clientObj in connections.values():
            # self.conn.send(message.encode())
            clientObj.send(message.encode())

    def listener(self, username, conn):
        while True:
            try: 
                message = conn.recv(1024).decode('utf-8')
                self.send_everyone(('<' + username + '>: ' + message))
            except:
                self.send_everyone((username + ' has left the chat'))
                del connections[username]
                return #ending the thread 


if __name__ == '__main__':
    server = ChatRoom('127.0.0.1', 1234)
    server.start()
    
        
