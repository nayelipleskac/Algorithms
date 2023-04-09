import math 

def distance(x1, y1, x2, y2):
    print(x1, ',', y1)
    print(x2, ',', y2)
    calc1= (x2-x1)**2
    calc2 = (y2-y1)**2
    calc3 = calc1 + calc2
    
    final_calc=math.sqrt(calc3)
    final_calc = round(final_calc,2)
    print('final_calc: ',final_calc)

def midpoint(x1, y1, x2, y2):
    calc1 = ((x1+x2)/2)
    calc2 = ((y2+y1)/2)
    calc3 = calc1, calc2
    print(calc3)


print('hello')

# X1 = int(input('Enter in x-coordinate for 1st point: '))
# Y1 = int(input('Enter in y-coordinate for 1st point: '))

# X2 = int(input('Enter in x-coordinate for 2nd point: '))
# Y2 = int(input('Enter in Y-coordinate for 2nd point: '))

# userInput= input('Do you want to calculate distance or midpoint: ')

# if userInput == 'distance':
#     distance(X1, Y1, X2, Y2)

# elif userInput == 'midpoint':
#     midpoint(X1, Y1, X2, Y2)

