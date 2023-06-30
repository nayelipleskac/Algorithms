from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import random, time
import sqlite3

class Phonebook(Tk):
    root = Tk()
    def __init__(self):
        Phonebook.root.geometry('400x400')
        self.myName = ''
        self.myPhone = ''
        self.phoneBookFrame = Frame(Phonebook.root, width = 400, height = 400)
        self.phoneText = Label(self.phoneBookFrame, text = 'Phonebook')
        self.nameEntry = Entry(self.phoneBookFrame)
        self.phoneEntry = Entry(self.phoneBookFrame)
        self.saveBtn = Button(self.phoneBookFrame, text = 'Save', command = self.addToDatabase)
        self.conn = sqlite3.connect('Nayeli.db')
        with self.conn:
            self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS phonebook (name string, phone string)')
    def packComponents(self):
        self.phoneBookFrame.pack()
        self.phoneText.pack()
        self.nameEntry.pack()
        self.phoneEntry.pack()
        self.saveBtn.pack()
    def addToDatabase(self):
        self.myName =self.nameEntry.get()
        self.myPhone = self.phoneEntry.get()
        print(self.myName, self.myPhone)
        self.cursor.execute('INSERT INTO phonebook(name, phone) VALUES (?,?)', (self.myName, self.myPhone))
        self.conn.commit()

if __name__ == '__main__':
    phonebook = Phonebook()
    phonebook.packComponents()
    Phonebook.root.mainloop()

#login and register application
#seach for phone# with name

# root = Tk()
# root.geometry('400x400')
# frame1 = Frame(root, bg = 'red', width = 400, height = 200)
# frame2 = Frame(root, bg = 'blue', width = 400, height = 200)
# frame1.pack()
# frame2.pack()
# root.mainloop()