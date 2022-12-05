##################################
# insertion sort algorithm
# big O notation : O(n^2)
# space complexity: O(1)
# runtime using timeit: 0.00001870 
##################################


import timeit, random, cProfile
from memory_profiler import profile
import requests

# def insertionSort(nums, current_index):
#     for i in range(1, len(nums)): 
#         key = nums[i]
#         j = i-1
#         while j >= 0 and key < nums[j]:
#             nums[j+1]  = nums[j] 
#             j = j - 1
#         nums[j+1] = key


# nums= [5,18,22,13,70,1,7] 
# current_index = nums[1]
# print('unsorted list: ', nums)
# insertionSort(nums, current_index)
# print('sorted list using insertion: ', nums)

# t = timeit.timeit(stmt=lambda: insertionSort(nums, current_index), number = 1)
# t=round(t,8)
# print('runtime for selection sort: {:.8f} secs using TIMEIT\n'.format(t))

##########################
#recursive insertion sort
# space complexity: O(1)
# runtime: 0.00000480 secs
# time complexity: O(n^2)
##########################
@profile
def insertionSort(nums, n):
    if n <= 1:
        return 0
    else: 
        insertionSort(nums, n-1)
        key= nums[n-1] 
        j = n-2
       
        while j >= 0 and key<nums[j]:
            # print('nums list',nums)
            nums[j+1]  = nums[j] 
            j = j-1
        nums[j+1] = key
                

nums = [5,18,22,13,70,1,7]
current_index = len(nums)
print('unsorted list: ', nums)
insertionSort(nums, len(nums))
print('sorted list: ', nums)

# cProfile.run(insertionSort(nums, current_index))

t = timeit.timeit(stmt=lambda: insertionSort(nums, current_index), number = 1)
t=round(t,8)
print('runtime for insertion sort: {:.8f} secs using TIMEIT\n'.format(t))