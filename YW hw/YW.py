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
# import random
# nums= {}

# for x in range(5):
#     num = random.randint(1,50)
#     square = num**2
#     nums[num] = square

# print(nums)
# num_values =list(nums.values())
# minimum = min(num_values)
# maximum = max(num_values)
# print('min: ', minimum)
# print('max:', maximum)

##########
#june 29th
##########
import random, time
# angelNums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]
# while True:
#     num=random.randint(1000,9999)
#     print(num)
#     time.sleep(0.5)
#     if num in angelNums:
#         print('woah- angel numbers!!')
#         time.sleep(2)
#         #continue until numbers add to 10
#         digit1 = num // 1000
#         digit2 = (num//100) % 10
#         digit3 = (num//10) % 10
#         digit4 = num % 10
#         digit_sum = digit1 + digit2 + digit3 + digit4
#         if digit_sum == 10:
#             print(num,' adds up to 10!')
#             break

#july 3
# train_mph = 100
# train_time = 60
# train_time = train_time / 4
# train_mph = train_mph / 4
# print('the train\'s mph is ', train_mph, 'and it takes ', train_time, 'minutes')

#july 16
# dice = int(input('how many dice: '))

# def calculate_outcomes(dice):
#     outcomes = 6** dice
#     return outcomes

# total = calculate_outcomes(dice)

# print('the total outcomes are ', total, 'of rolling ', dice, 'dice')

#july 23
# import random, time
# num1 = random.randint(1,10)
# num2 = random.randint(1,10)
# time_input = int(input('how many secs do you want to wait? 1-5 '))
# time.sleep(time_input)
# if num1 == num2:
#     print('the nums are equal!!')
# else:
#     print('the nums are not equal ://')
# a=b=c= 'Apple'

# print (a)

# print (b)
 
# print (c)

# num1 = input('Number 1: ')
# num2 = input('Number 2: ')
# num3 = input('Number 3: ')
# num4 = input('Number 4: ')
# output1 = num1+ num2+  num3+  num4
# output2 = num1 + '' + num2 + ''+ num3 + ''+ num4

# print('Output:', output1)
# print('Output: ', output2)

# input1 = input('Enter first string: ')
# input2 = input('Enter second string: ')
# print(input1, '\n', input2)
# print(input1+input2, end = '')

# num1 = float(input('decimal number input:  '))
# rounded_num = round(num1, 2)
# print(rounded_num)

# name = 'nayeli'
# num = str(9)
# decimal = str(19.89)
# print('My name is ' + name + ' my number is ' + num + ' and my fav decimal num is ' + decimal)


# height = float(input('How tall are you in cm? '))
# height = height / 30.48
# rounded_height = round(height, 2)
# print('so you are ', rounded_height, 'ft tall')

# pi = 3.14
# radius = 6370
# earth_area = 4*pi*(radius^2)
# print('the earth\s area is: ', earth_area, 'km')
# land_area =.30 * earth_area
# print('and the area that is land is: ', land_area, 'km')

# num = '123456'
# if '7' in num: 
#     print('yes')
# else: 
#     print('no')
# num = ((4*5)/2)*8+2/42
# rounded_num = int(num) 
# print(rounded_num)
# import time
# def swap(b1, b2):
#     b1 = 'soda'
#     b2 = 'milk'
#     time.sleep(1)
#     print('bottle one is ', b1)
#     print('bottle two is ', b2)

# bottle_one = 'milk' 
# bottle_two = 'soda'
# print('bottle one is ', bottle_one)
# print('bottle two is ', bottle_two)
# swap(bottle_one, bottle_two)

# august 20
# a=234
# print(type(a))
# print(str(a))

# b=345.678
# print(type(b))
# print(int(b))

# c='765'
# print(type(c))
# print(float(c))

# d=890.345
# print(type(d))
# print(str(d))

# e= '4765'
# print(type(e))
# print(int(e))

# print(round(-1.0932))

# print(round(98.987))

# print(round(5.555))

# print(round(8749))

# int1 = int(input('1: '))
# int2 = int(input('2: '))

# float_val = float(f'{int1}.{int2}')
# print('the float value is: ', float_val)
# print('the square of the float is: ', float_val ** 2)

# age = input('age: ')
# dob = input('year of birth: ')
# password = dob + '.' + age + '!'
# print(password)

# age = 16
# age_str = str(age)
# sum_of_digits = 0

# for digit in age_str:
#     if digit.isdigit():
#         sum_of_digits += int(digit)
# print(f"The sum of digits in your age is: {sum_of_digits}")

#August 27
# import math
# def calculate(a, b):
#     lcm = (a*b)//math.gcd(a,b)
#     print('the least common multiple is: ', lcm)


# num1 = int(input('First number: '))
# num2 = int(input('Second number: '))
# calculate(num1, num2)

#August 31st

# import math

# def is_perfect_cube(num):
#   cube_root = math.pow(num, 1/3)
#   return cube_root.is_integer()

# print(is_perfect_cube(27)) # True
# print(is_perfect_cube(28)) # False

# def count_types(input_list):
#   float_count = 0
#   int_count = 0 
#   string_count = 0
#   bool_count = 0
  
#   for item in input_list:
#     if isinstance(item, float):
#       float_count += 1
#     elif isinstance(item, int): 
#       int_count += 1
#     elif isinstance(item, str):
#       string_count += 1  
#     elif isinstance(item, bool):
#       bool_count += 1
      
#   print(f"Floats: {float_count}") 
#   print(f"Integers: {int_count}")
#   print(f"Strings: {string_count}")
#   print(f"Booleans: {bool_count}")

# mixed_list = [1.2, 5, "abc", 'True', 3, 2.5]
# count_types(mixed_list)

# def factors(num):
#   factors = []
  
#   for i in range(1, num + 1):
#     if num % i == 0:
#       factors.append(i)
      
#   return factors

# number = 120

# print(factors(number))

# pattern = "xoxoxo"

# for i in range(3):
#   if i%2 == 0:
#     print(pattern)
#   else:
#     print(pattern[::-1])

# From 1 to 40
# for i in range(1, 41):
#   if i%3==0 and i%2!=0:
#     print(i, end=' ') 

# print('\n')
# # From 41 to 60   
# sum = 0
# for i in range(41, 61):
#   sum += i
# print(sum)

# print('\n')

# # From 61 to 100
# for i in range(61, 101):
#   if i%4==0:
#     print(i, end=' ')
# import random
# first_sum = 0
# second_sum = 0
# for i in range(20):
#     num=random.randint(1,15)
#     if i < 10: 
#         first_sum += num
#     else:
#         second_sum += num
# print('first sum: ', first_sum)
# print('second sum: ', second_sum)

# days = int(input("Enter number of days in month: "))

# print("M T W T F S S")

# day = 1
# for i in range(days//7 + 1):
#   for j in range(7):
#     if day <= days:
#       print(str(day).rjust(2), end=' ')
#       day += 1
#     else:
#       print('  ', end=' ')  
#   print()

# books = ['the giver', 'hunger games', 'little women', 'happy place', 'divergent']
# books.reverse()
# for i in books: 
#     print(i)
    # print('\n')

###########
#October 12
###########

# num1 = input('enter a floating point number: ')
# try: 
#     float_value = float(num1)
#     decimal = float_value - int(float_value)
#     print(f'the float of the number is: {decimal:.4f}')
# except ValueError: 
#     print('wrong input. please enter a floating point number...')

# # Create a function that converts binary string to hex
# str = input('enter a binary string')

# input1 = input('Enter numbers for the first group separated by spaces: ')
# group1 = set(map(int, input1.split()))

# input2 = input('Enter numbers for the first group separated by spaces: ')
# group2 = set(map(int, input2.split()))

# result_group = group1-group2
# print("Numbers in the first group after removing those in the second group:")
# print(sorted(result_group)) 

############################### 
# converts binary string to hex
###############################

# def binary_to_hex(binary_str):
#     # Ensure the binary string has a '0b' prefix and remove it if present
#     if binary_str.startswith('0b'):
#         binary_str = binary_str[2:]

#     # Convert the binary string to an integer
#     decimal_value = int(binary_str, 2)

#     # Convert the decimal integer to a hexadecimal string
#     hex_str = hex(decimal_value)

#     return hex_str


# binary_str = "11010101"
# hexadecimal_str = binary_to_hex(binary_str)
# print("Binary:", binary_str)
# print("Hexadecimal:", hexadecimal_str)


############
# October 26
############
# import time
# word = input('Enter a word with 6 letters in it: ')
# for letter in word: 
#     print(letter)
#     time.sleep(0.5)

# import time, random
# userinput = int(input('Enter a number and I will tell you a random number between 1 and the number (number cannot be 1): '))
# random_num = random.randint(1, userinput)
# time.sleep(2)
# print(random_num)

# random_hour = random.randint(0,23)
# random_minute = random.randint(0,59)
# random_second = random.randint(0,59)
# random_time = f'{random_hour}:{random_minute}:{random_second}'
# print(random_time)
# wait_time = int(input('enter the wait duration in seconds: '))
# #input time seconds to hours, mins, secs
# newHour = wait_time // 3600
# remainder = wait_time % 3600   

# newMinutes = wait_time // 60
# newSeconds = wait_time // 60

# finalhour=(random_hour + newHour) % 24 
# finalmin= (random_minute + newMinutes) % 60
# finalsec= (random_second + newSeconds) % 60

# print(f'{finalhour}:{finalmin}:{finalsec}')

############
# October 29
############
# strinput = input('enter in a string: ')
# print(strinput[-3:])
# print(strinput[3:])
# for index, letter in enumerate(strinput): 
#     print(f'{index}: {letter}')

# userinput = input('enter a string: ')
# vowels = ['a', 'e', 'i', 'o', 'u']
# newword = ''
# for letter in userinput: 
#     if letter in vowels:
#         newword +='-'
#     else:
#         newword += letter
# print(newword)

# def wordsInString(userInput):
#     words = userInput.split()
#     numwords = len(words)
#     print('words in the string:', numwords)

# def letters(userInput):
#     count = 0
#     for char in userInput:
#         if char.isalpha() or char.isspace():
#             count+=1
#     print('letters in string:', count)

# total_chocolates = int(input('Enter the total number of chocolates in the box: '))
# num_children = int(input("Enter the number of children present at the party: "))
# chocolates_per_child = total_chocolates // num_children
# chocolates_for_birthday_girl = total_chocolates % num_children
# print(f"The birthday girl got {chocolates_for_birthday_girl} chocolates. The rest of the children got {chocolates_per_child} chocolates.")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# result_a = num1 ** num2 + num3 ** 2
# result_b = num1 ** 3 + num2 ** 3 + num3 ** 3
# result_c = (num1 * num2 * num3) ** num2
# result_d = (num1 ** 2 + num2 ** 2 + num3 ** 2) / (num1 + num2 + num3)

# print(f"a) {num1} to the power of {num2} + {num3} squared is {result_a}")
# print(f"b) The sum of the cubes of {num1}, {num2}, and {num3} is {result_b}")
# print(f"c) The result of ({num1} * {num2} * {num3}) to the power of {num2} is {result_c}")
# print(f"d) The sum of the squares of {num1}, {num2}, and {num3} divided by their sum is {result_d}")

# import random
# random_nums = []
# for i in range(3):
#     random_int = random.randint(1,10)
#     random_nums.append(random_int)

# if random_nums[1] > max(random_nums[0], random_nums[2]):
#     print('Yay')
# else:
#     print('no')
# import random
# num1 = random.randint(5,15)
# num2 = random.randint(5,15)
# num3 = random.randint(5,15)
# print(num1, num2, num3)

# if (num1+num2) > num3 and (num2+num3) > num1 and (num1+num3) > num2:
#     print('a triangle can be formed')
# else: 
#     print('a triangle cannot be formed ')

# import random
# counter = 0
# positve_num = [1,2,3,4,5,6,7,8,9,10]
# for i in range(5):
#     num=random.randint(-5,10)
#     if num== -7:
#         counter-= 1
#     elif num in positve_num:
#         counter += 1
#     print('num: ', num, 'counter: ', counter)

# def calculate_average_goals(goals_scored, games_played):
#     if games_played <= 0:
#         return "Invalid number of games played"
    
#     average_goals = goals_scored / games_played
#     return average_goals

# # Get user input for the number of goals scored and optional games played
# goals = int(input("Enter the total number of goals scored: "))
# games = int(input("Enter the number of games played: ") or 38)

# average = calculate_average_goals(goals, games)
# print(f"The average goals per game for the season is {average:.2f}")

# def calculate(num1, num2, sign):
#     if sign == '+':
#         print(num1 + num2)
#     elif sign == '-':
#         print(num1 - num2)
#     elif sign == '/':
#         print(num1 / num2)
#     elif sign == '*':
#         print(num1 * num2)
# num1 = int(input('number one: '))
# num2 = int(input('number two: '))
# sign = input('sign: ')
# calculate(num1, num2, sign)


from datetime import datetime

def calcAgeDiffDays(birthdate1, birthdate2=None):
    if birthdate2 is None:
        birthdate2 = datetime(2006, 12, 3)
    elif not isinstance(birthdate1, datetime) or not isinstance(birthdate2, datetime):
        return "Invalid input. Please provide valid birthdates as datetime objects."
    
    age_difference = abs((birthdate1 - birthdate2).days)
    return age_difference

#example
my_birthdate = datetime(2006, 12, 3)
your_birthdate = datetime(2000, 7, 8)
age_diff = calcAgeDiffDays(my_birthdate, your_birthdate)
print(f"You are {age_diff} days older/younger than me.")




