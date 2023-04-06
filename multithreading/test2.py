# import test_txt 

# file = open("answers.txt","r")
# lines = file.read()
# print(lines)

with open('answers.txt', 'r') as file:
    contents = file.read()
    print(contents)
