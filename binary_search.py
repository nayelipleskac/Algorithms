#finished runtime thing; binary search
#with recursion
#assuming the list is sorted ..
#set 3
#iterative
import random, time, timeit

##########################################
## iterative binary search
## binary search algorithm with while true
##########################################

# nums = [3,6,13,8,23,21]

# nums.sort()
# x= random.choice(nums)
# min_index = 0  
# max_index = len(nums)-1

# print('random num: ', x)
# time.sleep(2)
# print(nums)
# # value_mid_index = nums[mid_index]
# while True: 
#     if max_index < min_index:
#         break 

#     mid_index = (min_index + max_index) // 2
#     if x == nums[mid_index]: 
#         print('Number was found', x, 'index: ', mid_index)
#         break
#     elif x > nums[mid_index]: 
#         min_index = mid_index + 1
#     elif x < nums[mid_index]:
#         max_index = mid_index -1

####################################################
## recursive binary search
## binary search algorithm with recursion and timeit
## time complexity: O(log(n)) algorithm - searching sorted array
## space complexity: O(1)
####################################################

def binarySearch(nums, x, min_index, max_index):
    if max_index>=min_index:
        mid_index = (min_index + max_index) // 2
        if max_index < min_index: #base case 1 if x doesn't exist
            return -1
        if x == nums[mid_index]: #base case 2 when x is found 
            print('Number was found: ', x, 'index', mid_index)
            return mid_index 

        elif x > nums[mid_index]: #x greater than median
            return binarySearch(nums, x, mid_index+1, max_index)

        elif x < nums[mid_index]: #x smaller than median
            return binarySearch(nums,x,min_index, mid_index-1)
        

nums = [3,6,13,8,23,21]
nums.sort()
x= random.choice(nums)
min_index = 0  
max_index = len(nums)-1
# binarySearch(nums, x, min_index, max_index)

t= timeit.timeit(stmt=lambda: binarySearch(nums,x,min_index,max_index), number = 1)
t = round(t,8)
print('exeuction time using timeit : {:.8f} sec\n'.format(t))


