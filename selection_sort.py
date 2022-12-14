#Selection Sort

import timeit, random

############################
# selection sort algorithm
# big O notation : O(n^2) 
# omega notation: O(n^2)
# runtime using timeit 
############################

# def selectionSort(nums, numsLength):
#     for x in range(numsLength):
#         min_index = x 
#         # min_index+1
#         for y in range(x+1, numsLength):
#             if nums[y] < nums[min_index]:
#                 #swap elements from unsorted to sorted
#                 min_index = y
#                 (nums[x], nums[min_index]) = (nums[min_index], nums[x])
#                 # print(nums)
#     # return nums

# nums= [5,18,22,13,70,1,7] 
# min_index = 0
# numsLength = len(nums)

# print('unsorted list: ', nums)
# selectionSort(nums, numsLength)
# print('sorted list: ')
# print(nums)

# t = timeit.timeit(stmt=lambda: selectionSort(nums, numsLength), number = 1)
# t=round(t,8)
# print('runtime for selection sort: {:.8f} secs using TIMEIT\n'.format(t))

#####################################
# recursive version of selection sort 
# time complexity: O(n^2) 
# space complexity: O(1)
# runtime: 0.00000470 secs
#####################################
def selectionSort(nums, numsLength, x):
    if numsLength == 0:
        return 
    else: 
        # for x in range(numsLength):
            min_index = x
            for y in range(x+1, numsLength):
                if nums[y] < nums[min_index]:
                    min_index = y
                    (nums[x], nums[min_index]) = (nums[min_index], nums[x])
                    #recursive call here ? 
                    if x + 1 < numsLength:
                        selectionSort(nums, numsLength, x + 1)

nums = [5,18,22,13,70,1,7] 
min_index = 0
numsLength = len(nums)
print('unsorted list: ', nums)
selectionSort(nums, numsLength, 0)
print('sorted list with recursion: ')
print(nums)

t = timeit.timeit(stmt=lambda: selectionSort(nums, numsLength, 0), number = 1)
t=round(t,8)
print('runtime for selection sort: {:.8f} secs using TIMEIT\n'.format(t))
