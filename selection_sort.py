#Selection Sort

import timeit, random

############################
# selection sort algorithm
# big O notation : O(n^2) 
# omega notation: O(n^2)
# runtime using timeit 
############################

def selectionSort(nums, numsLength):
    for x in range(numsLength):
        min_index = x 
        # min_index+1
        for y in range(numsLength+1, numsLength):
            if nums[y] < nums[min_index]:
                #swap elements from unsorted to sorted
                min_index = y
                (nums[x], nums[min_index]) = (nums[min_index], nums[x])
                # print(nums)
    # return nums

nums= [2,1,6,7,10,5] 
min_index = 0
numsLength = len(nums)

# print('unsorted list: ', nums)
print('sorted list: ')
selectionSort(nums, numsLength)

t = timeit.timeit(stmt=lambda: selectionSort(nums, numsLength), number = 1)
t=round(t,8)
print('runtime for program: {:.8f} secs using TIMEIT\n'.format(t))