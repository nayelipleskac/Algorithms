# client 
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

def create_thread(target):
    t= Thread(target=target)
    t.daemon = True
    t.start()

class Game(socket.socket,Tk):
    def __init__(self, host = socket.gethostname(), port = 1234):
        Tk.__init__(self)
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)

        self.title('Full Duplex Messaging App: Client')
        self.geometry('400x400')
        self.top_frame = Frame(self)
        self.text_area = Text(self.top_frame, height =  20, width = 50)
        self.bottom_frame= Frame(self)
        self.entry = Entry(self.bottom_frame, width= 40)
        self.send_button = Button(self.bottom_frame, text = 'Send', command = self.send_message)
        
        self.host = host
        self.port = port
        self.na = socket.gethostname()
    def start(self):
        print('host:', self.host)
        self.connect((self.host, self.port))
        # self.sendall('Client: connection established'.encode())
        print('Client: Connected to {}'.format(self.host, self.na))
        self.pack_components()
        create_thread(self.accept_message)

    def pack_components(self):
        self.top_frame.pack(pady=10)
        self.text_area.pack(side = LEFT, padx= 10)
        self.text_area.tag_configure('right_align', justify='right')
        self.bottom_frame.pack(pady=10)
        self.entry.pack(padx= 10, side=LEFT)
        self.send_button.pack(side= LEFT)
    def send_message(self):
        #self.accept message
        create_thread(self.accept_message)
        #enter message to send
        message = self.entry.get()
        self.text_area.insert(END, message + '\n', 'right_align')
        self.entry.delete(0, END)
        self.send(message.encode())
    def accept_message(self):
        while True:
            data = self.recv(1024).decode()
            if not data:
                break
            print('Received from server: ', data)
            self.text_area.insert(END, data + '\n', 'left_align')
                

if __name__ == '__main__':          
 
    game = Game('127.0.0.1', 1234)
    game.start()
    game.mainloop()
