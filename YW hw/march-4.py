# import line_functions.py
# line_functions.distance()

from line_functions.py import distance, midpoint

X1 = int(input('Enter in x-coordinate for 1st point: '))
Y1 = int(input('Enter in y-coordinate for 1st point: '))

X2 = int(input('Enter in x-coordinate for 2nd point: '))
Y2 = int(input('Enter in Y-coordinate for 2nd point: '))

userInput= input('Do you want to calculate distance or midpoint: ')
if userInput == 'distance':
    distance(X1, Y1, X2, Y2)

elif userInput == 'midpoint':
    midpoint(X1, Y1, X2, Y2)