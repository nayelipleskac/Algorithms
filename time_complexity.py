#time complexity examples using O(n)
import random, time, timeit


####################
# O(n) equation
# using one for loop
####################

# nums= [1,3,5,7,9,11,13,15]
# for i in nums:
#     print('O(n) represented by : ', i, ' index: ', nums.index(i))


#############################
# O(n+m) equation
# using 2 different for loops
#############################

nums= [1,3,5,7,9,11,13,15]
for i in nums:
    print('O(n+m) ', i)
for x in nums:
    print('index of x : ', nums.index(x))

##################################
# O(n^2)
# nested for loops same collection
##################################
oddNums= [1,3,5,7,9,11,13,15]
# evenNums = [2,4,6,8,10,12,14,16]
# for i in range(1,10)
#     for j in evenNums:
#         print(i,j)
