from threading import Thread
from time import sleep
import random, numpy

#hw: questions 1-3 on multithreading 

# def print_double(num):
#     print('The double of {} is {} '.format(num, num*2))
# double_maker = Thread(target = print_double, args = (10,))
# double_maker.start()
# print('Thread ended')

# def get_squares(start, end):
#     for num in range(start, end+1, 1):
#         print('The square of {} is {} '.format(num, num*num))
# square_thread = Thread(target = get_squares, args = (10,20))
# square_thread.start()
# square_thread.join()
# print('Message 1')
# print('Message 2')
# print('Message 3')

# def prime_checker(num):
#     prime = True
#     for d in range(2, int(num**0.5) +1, 1):
#         print('{} checked with {}'.format(num,d))
#         if num % d == 0:
#             prime = False
#         if prime == True: 
#             print('{} is a prime number'.format(num))
#         else:
#             print('{} is not a prime number'.format(num))

# def primes(numbers):
#     for num in numbers:
#         t = Thread(target = prime_checker, args = (num,))
#         t.start()
#         # t.join()
#         print('Completed task for {}!'.format(num))

# prime_thread = Thread(target = primes, args = ([4483,4493,4507,4561,4567,4583,4591],))
# prime_thread.start()
# # prime_thread.join()
# print('The program ended')

##################
##question 1 and 2
################## 

# letters = ['A', 'B', 'C', 'D']
# def func():
#     for letter in letters:
#         print(letter)
#         sleep(2)
# thread = Thread(target = func)
# thread.start()
# print('E')

## hw 11/27

# explain every picture in introduction slides next class
# insert code for all alogorithms
# explain singleton design pattern 

def number_printer1():
    for number in range(1,6,1):
        print(number)
        sleep(1)
    print('numberprinter1 finished')

def number_printer2():
    for number in range(1,11,1):
        print(number)
        sleep(1)
    print('numberprinter2 finished')
thread1, thread2 = Thread(target = number_printer1), Thread(target = number_printer2)
thread1.start()
thread2.start()
print('threads started')
thread1.join()
thread2.join()
print('threads finished')



###########
#question 3
###########
# numbers = [[],[],[],[],[]]
# def randomNumbers():    
#     for i in range(0,5,1):
#         for j in range(0,10,1): #10 random integers
#             numbers[i].append(random.randint(1,15))        
#     # print(numbers)
#     # print(numpy.prod(numbers[0]))
#     # print(numpy.prod(numbers[1]))
#     # print(numpy.prod(numbers[2]))
#     # print(numpy.prod(numbers[3]))
#     # print(numpy.prod(numbers[4]))


# for i in range(0,5,1):
#     thread = Thread(target = randomNumbers)
#     thread.start()
#     print(numbers[i])
#     print(numpy.prod(numbers[i]))






