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

root =  tk.Tk()
root.title('Full Duplex Client')
root.geometry('180x200')


# class Client(socket.socket):
#     def __init__(self, host = socket.gethostname(), port = 1234):
#         super().__init__(socket.AF_INET, socket.SOCK_STREAM)

class Client:
    def __init__(self, root):
        self.root = root
        self.frame1 = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root)
        self.label1 = tk.Label(self.frame1, text = 'Enter Message: ')
