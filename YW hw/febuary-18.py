def returnWord(userInput, constants):
    word=userInput
    print(word)
    for letter in word:
        if letter == 'a' or letter == 'o' or letter == 'e' or letter == 'i' or letter == 'u': 
            print(letter, 'is a vowel')
        else:
            constants.append(letter)
            print(letter, 'is a constant')
        
constants = []
userInput = input("Enter a string: ")
returnWord(userInput, constants)
print(constants)

#num = int(input('Enter a number: '))
for num in range(1,1000,1):
    num_digits = len(str(num))
    sum = 0
    for digit in str(num):
        sum += int(digit) ** num_digits

    if sum == num:
        print(num, 'is an armstrong num!')
##    else:
##        print(num, 'is not an armstrong num')

    
