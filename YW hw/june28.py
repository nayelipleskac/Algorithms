from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random, time
import sqlite3

#seach for phone# with name
#login and register application with search
#Phonebook

class Phonebook(Tk):
    root = Tk() #not needed if class Phonebook is inheriting Tk
    def __init__(self):
        Phonebook.root.geometry('400x400')
        self.myName = ''
        self.myPhone = ''
        self.phoneBookFrame = Frame(Phonebook.root, width = 400, height = 400)
        self.phoneText = Label(self.phoneBookFrame, text = 'Phonebook')
        self.nameEntry = Entry(self.phoneBookFrame)
        self.phoneEntry = Entry(self.phoneBookFrame)
        self.saveBtn = Button(self.phoneBookFrame, text = 'Save', command = self.addToDatabase)
        self.loginBtn = Button(self.phoneBookFrame, text = 'Login', command = self.login, bg = 'red')
        self.registerBtn = Button(self.phoneBookFrame, text = 'Register', command = self.register, bg = 'green')
        self.searchBtn = Button(self.phoneBookFrame, text = 'Search', command = self.search)
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
        self.searchBtn.pack()
        self.loginBtn.pack()
        self.registerBtn.pack()
    def addToDatabase(self):
        self.myName =self.nameEntry.get()
        self.myPhone = self.phoneEntry.get()
        print(self.myName, self.myPhone)
        self.cursor.execute('INSERT INTO phonebook(name, phone) VALUES (?,?)', (self.myName, self.myPhone))
        self.conn.commit()
        self.nameEntry.delete(0,END)
        self.phoneEntry.delete(0, END)
    def search(self):
        self.myName = self.nameEntry.get()
        self.cursor.execute('SELECT phone FROM phonebook WHERE name = ?', (self.myName,))
        phone_number = self.cursor.fetchone()
        self.phoneEntry.delete(0, END)
        if phone_number:
            self.phoneEntry.insert(0, phone_number[0])
        else:
            messagebox.showinfo('No data', 'No data found for this name')
    def login(self):
        self.myName =self.nameEntry.get()
        self.myPhone = self.phoneEntry.get()
        self.cursor.execute('SELECT * FROM phonebook WHERE name = ? and phone = ?', (self.myName, self.myPhone))
        name = self.cursor.fetchone()
        if name:
            messagebox.showinfo('welcome', 'welcome {}!'.format(name[0]))
        else:
            messagebox.showinfo('No data', 'No data found for this name')
    
    def register(self):
        pass

if __name__ == '__main__':
    phonebook = Phonebook()
    phonebook.packComponents()
    phonebook.mainloop() #or Phonebook.root.mainloop()



