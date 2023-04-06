import threading, time, random

################################################
# hw: repeat previous exercises with inheritance
################################################

# class Hello(threading.Thread):
#     def __init__(self, min, max):
#         self.min, self.max = 1,3
#         threading.Thread.__init__(self, min, max)

        # time.sleep(self.max)
        # for i in range(1000):
        #     print(random.choice(range(self.min, self.max)))
#This creates the thread objects, but they don't do anything yet.
# h = Hello(1,3)
# k = Hello(0,3)

#This causes each thread to do its work
# h.start()
# k.start()

#example 1
# class MyThread(threading.Thread):
#     def run(self):
#         print('run function')

# if __name__ == '__main__':
#     for i in range(3):
#         t = MyThread()
#         t.start()

###########
# problem 1
###########

# letters = ['A', 'B', 'C', 'D']
# def func():
#     for letter in letters:
#         print(letter)
#         sleep(2)
# thread = Thread(target = func)
# thread.start()
# print('E')

##################
# with inheritance
##################

# from time import sleep

# class MyThread(threading.Thread):
#     def run(self):
#         self.letters= ['A', 'B', 'C', 'D']
#         for letter in self.letters:
#             print(letter)
#             sleep(2)
#         print('E')
    
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()
    
###########
# problem 2
###########
from threading import Thread

# def number_printer():
#     for number in range(1,6,1):
#         print(number)
#         time.sleep(1)
    
# thread = Thread(target = number_printer)
# thread.start()
# print('A')
# thread.join()
# print('B')

##################
# with inheritance
##################

class MyThread(Thread):
    def number_printer(self):
        print('in number_printer')
        for number in range(1,6,1):
            if number == 1:
                print('A')
            print(number)
            time.sleep(1)
        print('B')
    def run(self):
        self.number_printer()

if __name__ == '__main__':
    thread = MyThread()
    thread.start()
    thread.join()


