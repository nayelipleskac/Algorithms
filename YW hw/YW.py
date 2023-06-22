# list2 = []
# for i in range(1,6):
#     list1 = []
#     word1 = input('Enter in a word: ')
#     list1.append(word1)
#     reverse_word = word1[::-1]
#     list1.append(reverse_word)
#     list2.append(list1)
#     print(reverse_word)
# print(list2)
# 
# 
# def check(number,numLength):
#     for x in numLength:
#         if x == '.':
#             return
#         else:
#             x = '*'
#     print(number)

# numInput = (input('Enter a number: '))
# check(numInput,len(numInput))

#astericks excersise
 
# numInput = (input('Enter a number: '))
# if '.' in numInput: 
#     integar_part, decimal_part = numInput.split('.')
#     integar_part = '$'*len(integar_part)
#     decimal_part = '$'*len(decimal_part)
#     print(integar_part+'.'+decimal_part)
# else:
#     newWord = '$' * len(numInput)
#     print(newWord)

#random nums

# import random
# x = random.randint(0,500)
# y = random.randint(0,500)
# z = random.randint(0,500)

# print(x,y,z)
# if x > y and x>z:
#     print('The largest is: ', x)
# if y > z and y>x:
#     print('The largest is: ', y)
# if z > x and z> y:
#     print('The largest is: ', z)

# shapes={'square':4, 'circle':0, 'hexagon':6, 'decagon':10}

# userShape = input('What is your favorite shape? ')
# if userShape in shapes:
#     print(userShape, shapes[userShape])
# else: 
#     sides = input('How many sides in this shape? ')
#     shapes[userShape] = sides
#     print(shapes)

#naming

# while True:
#     nameInput = input('Enter a name: ')
#     if 'a' not in nameInput:
#         print('Aha! Name doesn\'t have an a in it! Goodbye')
#         break

# import datetime
# current_datetime = datetime.datetime.now()
# formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# with open('log.txt', 'a') as log_file:
#     user_input = input('Enter something to be logged: ')
#     #write user input to file
#     log_file.write(formatted_datetime + ' - ' + user_input + '\n')

# def returnWord(userInput, constants):
#     word=userInput
#     print(word)
#     for letter in word:
#         if letter == 'a' or letter == 'o' or letter == 'e' or letter == 'i' or letter == 'u': 
#             print(letter, 'is a vowel')
#         else:
#             constants.append(letter)
#             print(letter, 'is a constant')
        
# constants = []
# userInput = input("Enter a string: ")
# returnWord(userInput, constants)
# print(constants)

###########################################################################
# emunerate function is used to loop over an iterable (list, tuple, string) 
# along with an index that keeps track of the current iteratoin number
###########################################################################

# s = 'this is a sentence'
# result = ''
# for i,c in enumerate(s):
#     if i % 2==0:
#         result +=c.upper()
#     else:
#         result += c.lower()
# print(result)

# userInput = int(input('enter a number: '))
# numDict = {}
# for i in range(1,11,1):
#     numDict[i] = i**i
# print(numDict)

# def returnWord(userInput, constants):
#     word=userInput
#     print(word)
#     for letter in word:
#         if letter == 'a' or letter == 'o' or letter == 'e' or letter == 'i' or letter == 'u': 
#             print(letter, 'is a vowel')
#         else:
#             constants.append(letter)
#             print(letter, 'is a constant')
        
# constants = []
# userInput = input("Enter a string: ")
# returnWord(userInput, constants)
# print(constants)

# num = int(input('Enter a number: '))
# for num in range(1,1000,1):
#     num_digits = len(str(num))
#     sum = 0
#     for digit in str(num):
#         sum += int(digit) ** num_digits

#     if sum == num:
#         print(num, 'is an armstrong num!')
# #    else:
# #        print(num, 'is not an armstrong num')

##########
# march 17, 
##########
# import random

# count = {}

# for i in range(100):
#     number = random.randint(1,10)
#     if number in count:
#         count[number] +=1
#     else:
#         count[number] = 1

# print(count)

##########
# march 19
##########

# def giveName(name):
#     if name == '':8

#         print('Hello Guys')
#     else:
#         print('Hello', name)

# nameInput = input('Hello! What\'s your name? ')
# giveName(nameInput)

#hw for april 9th
# numList = []
# while True: 
#     numInput = int(input('Enter a random number: '))
#     newList = [numInput]
#     numList = newList + numList
#     # print(newList)
#     if numInput == -1:
#         print(numList)
#         print('done!')
#         break

#hw for april 9th
# import random
# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#A. replace all the elements with the square of the numbers and print the list
# def square(numsList):
#     for sublist in range(len(numsList)): 
#         for num in range(len(numsList[sublist])):
#             square_num = num **2
#             numsList[sublist][num] = numsList[sublist][num] ** 2
#     print(numsList)
# print(numbers)
# square(numbers)

#B- adding random nums
# def addRandomNumber(numbers): #to each sublist
#     for sublist in numbers:
#         sublist.append(random.randint(1,100))
# print(numbers)
# addRandomNumber(numbers)
# print(numbers)

#C. replace all the elements with 0 and print the list
# def replace(numbers): 
#     for sublist in range(len(numbers)):
#         for num in range(len(numbers[sublist])):
#             numbers[sublist][num] = numbers[sublist][num] * 0
#     print(numbers)
# replace(numbers)

##april 30th

# nameInput= input('Enter your name: ')
# languageInput= input('How many languages do you speak: ')
# print(nameInput, 'can speak', languageInput, 'languages!')

##may 28th
# first_name_input = input('Enter your first name: ')
# last_name_input = input('Enter your last name: ')
# print(first_name_input[0] + last_name_input[0])

## Find the data type of the following:

# num1 = 6452
# num2= -635.125
# s1 = '@#$%&'
# s2=  'jim-jam-joe'
# num3= 717171
# num4= 7
# num5 = 000.000111
# print(type(num1))
# print(type(num2))
# print(type(s1))
# print(type(s2))
# print(type(num3))
# print(type(num4))
# print(type(num5))

#may 30
# def create_usernames(first_name, last_name, fav_num):
#     username = first_name + '_' + last_name + '_' + fav_num
#     print('here is your username! \n', username)

# first_name_input =input('what is your first name? : ')
# last_name_input =input('what is your last name? : ')
# fav_num_input = input('and finally what is your favorite number? : ')
# create_usernames(first_name_input, last_name_input, fav_num_input)

#june 6
# books = {'dystopian':4, 'romance': 5, 'fantasy': 7, 'mystery': 3}
# print('Huray! You just went to the bookstore!')

# def bookstore(type):
#     q1 = input('Did you get any {} books? y/n '.format(type))
#     if q1 == 'y':
#         quantity = int(input('How many? '))
#         books[type] += quantity
#     elif q1 == 'n':
#         pass
# bookstore('dystopian')
# bookstore('romance')
# bookstore('fantasy')
# bookstore('mystery')
# print(books)

# q2 = input('Did you get any romance books? y/n ')
# if q2 == 'y':
#     quantity = int(input('How many? '))
#     books['romance'] += quantity
# elif q2 == 'n':
#     pass
# q3 = input('Did you get any fantasy books? y/n ')
# if q3 == 'y':
#     quantity = int(input('How many? '))
#     books['fantasy'] += quantity
# elif q3 == 'n':
#     pass
# q4 = input('Did you get any mystery books? y/n ')
# if q4 == 'y':
#     quantity = int(input('How many? '))
#     books['mystery'] += quantity
# elif q4 == 'n':
#     pass

###########
# june 19th
###########

# Create a dictionary with 5 random numbers from 1-50 as the keys and its square as their respective value. Print the maximum and minimum values from the dictionary.
import random
nums= {}

for x in range(5):
    num = random.randint(1,50)
    square = num**2
    nums[num] = square

print(nums)
num_values =list(nums.values())
minimum = min(num_values)
maximum = max(num_values)
print('min: ', minimum)
print('max:', maximum)