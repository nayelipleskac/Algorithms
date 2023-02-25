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
# newWord = '*' * len(numInput)
# print(newWord)

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
#     if 'a' in nameInput:
#         print('Aha! Name has an a in it! Goodbye')
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
#         result +=c.lower()
#     else:
#         result += c.upper()
# print(result)

userInput = int(input('enter a number: '))
numDict = {}
for i in range(1,11,1):
    numDict[i] = i**i
print(numDict)
