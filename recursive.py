

#exercise 1- linear search
# setup_code= 'from math import factorial'

import time, timeit, random
from stopwatch import Stopwatch
# start = time.time()
# nums = [2,4,6,8,10,12,14]
# num_var = random.choice(nums)
# for i in nums:
#         if i == num_var:
#             print('found the number:',i, ' index: ',nums.index(i))
#             break
#         else:
#             print('number not found:',i, ' index:', nums.index(i))

#####################################################################
## first linear search 
## linear search algorithm uisng runtime calculations (timeit.timeit)
## O(n)
#####################################################################

setup = '''
import random

nums = [2,4,6,8,10,12,14]
num_var = random.choice(nums)

def linearSearch(nums):
    for i in nums:
        if i == num_var:
            print('found the number:',i, ' index: ',nums.index(i))
            break
        else:
            print('number not found:',i, ' index:', nums.index(i))
'''
# start_time = timeit.default_timer()
# print('the starttime is, ', start_time)
# end = time.time()
# print('The time of execution of the linear search using time.time is: ', (end - start), 'ms') #0.0023 ms
# print(f"The time of execution of the linear search using timeit is:  {timeit.timeit(setup= setup, stmt = 'linearSearch', number = 1000000)}") # ms
# print('The time difference is : ', timeit.default_timer() - start_time)

#####################################################################
## second linear search - conclusion: timeit more efficient -
## linear search algorithm uisng runtime calculations (timeit.timeit)
## O(n)
#####################################################################

# nums = [2,4,6,8,10,12,14]
nums = [5,18,22,13,70,1,7,23,5,6,90,54,19,1,0,67,80,63,17,300,193,9384,823,4,95,98,288,234,4829,34,78]

# num_var = random.choice(nums)

def timeitLinearSearch(nums, num): #set of nums, target
    for i in nums:
        if i == num:
            # print('found the number:',i, ' index: ',nums.index(i))
            break
        # else:
        #     print('number not found:',i, ' index:', nums.index(i))

# t = timeit.Timer(stmt=lambda: linearSearch(nums), number = 1).timeit()
for i in nums:
    t = timeit.timeit(stmt=lambda: timeitLinearSearch(nums, i), number = 1)
    t=round(t,8)
    print('runtime for {}: {:.8f} secs using TIMEIT\n'.format(i,t))

###########################################################################
## third linear search 
## linear search algorithm uisng runtime calculations (stopwatch vs timeit)
## O(n^m)
###########################################################################

# nums = [2,4,6,8,10,12,14]

# def stopWatchLinearSearch(nums, num): #set of nums, target
#     stopwatch = Stopwatch()
#     stopwatch.start()
#     # t= stopwatch.
#     # t.start()
#     for i in nums:
#         if i == num:
#             # print('found the number:',i, ' index: ',nums.index(i))
#             stopwatch.stop()
#             print('time elapsed for {}: {:.8f} secs using STOPWATCH \n '.format(i, round(stopwatch.duration,8)))
#             break
#         # else:
#         #     print('number not found:',i, ' index:', nums.index(i))
        
# for i in nums:
#     stopWatchLinearSearch(nums,i)

#######################################
## recursive excersise 1
## recursive example to find factorials
## O(n^m)
#######################################

# def factorial(n):
#     if n is 1: #This is the base case
#         return 1  #when this condition holds true tells the program to stop and return all the values in sequential order.
#     return n * factorial(n-1)
# n = int(input("Number? "))
# print(factorial(n))

# t = timeit.timeit(stmt=lambda: factorial(n), number = 1)
# t=round(t,8)
# print('runtime for factorial using timeit : {:.8f} secs'.format(t)) 

###########################################################
## recursive excersise 2
## recusive example to find fibonacci sequence using timeit
## O(n^m)
###########################################################

# def fibonacci(n):
#     if n ==0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# n = int(input('Find the nth number in fibonacci sequence: ')) 
# #print just n
# print('number in sequence : ',fibonacci(n)) 
# t = timeit.timeit(stmt=lambda: fibonacci(n), number = 1)
# t= round(t,8)
# print('runtime for program : {:.8f} secs using timeit\n'.format(t))

# to print out sequence of n
# for i in range(n+1):
#     print(fibonacci(i))
#     t = timeit.timeit(stmt=lambda: fibonacci(n), number = 1)
#     t=round(t,8)
#     print('runtime for {} : {:.8f} secs using timeit\n'.format(x,t))
   

#######################################################
## recursive excersise 3
## recursive formula to find sums of digits with timeit
## O(n^m)
#######################################################

# print(123%10+(123//10))

#adding the sum of entered digits

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n%10+sum(n//10)

# n = int(input('Enter a number: '))

# print('sum: ', sum(n))
# t= timeit.timeit(stmt=lambda: sum(n), number = 1)
# t = round(t,8)
# print('time of program : {:.8f} sec\n'.format(t))


#########################################
## recursive excersise 4
## recursive formula to reverse a string
## O(n^m)
#########################################

# print('hello'[1:])
# def reverse(x):
#     if len(x) == 0:
#         return x 
#     else:
#         return reverse(x[1:]) + x[0]

# x = input('Enter a string: ')
# print(reverse(x))
# t= timeit.timeit(stmt=lambda: reverse(x), number = 1)
# t = round(t,8)
# print('time of program : {:.8f} sec\n'.format(t))

######################################
## recursive excersise 5
## pascal's triangle without recursion
######################################


# print(1)
# layer = [1, 1]
# layers = 1
# while layers < 10:
#     for elem in layer:
#         print(elem,end=' ')
#     print()
#     new_layer = []
#     for i in range(len(layer)-1):
#         num1 = layer[i]
#         num2 = layer[i+1]
#         new_layer.append(num1 + num2)
#     new_layer=[1] + new_layer + [1]
#     layer=new_layer
#     layers+=1

# ##############################################
## recursive excersise 5
## pascal's triangle with recursion and timeit
## time complexity: O(n*log(n)) sorting an element
## space complexity: O(1)
# ##############################################

# def pascal(layer): 
#     if len(layer) > 10:  #base cases
#         return
#     else: 
#         for i in layer:
#             print(i, end = ' ')
#         print()
#         new_layer = []
#         for i in range(len(layer)-1):
#             num1= layer[i]
#             num2 = layer[i+1]
#             new_layer.append(num1 + num2)

#         new_layer = [1] + new_layer + [1] 
#         layer = new_layer
#         pascal(layer)                                                                       
        
# print(1)
# layer = [1,1]
# # pascal(layer)
# t= timeit.timeit(stmt=lambda: pascal(layer), number = 1)
# t = round(t,8)
# print('time of program : {:.8f} sec\n'.format(t))





