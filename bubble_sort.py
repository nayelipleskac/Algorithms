#Bubble Sort

import timeit, random

#############################
## bubble sort algorithm
## runtime & time complexity:
## O(n^2)
############################# 

def bubbleSort(nums, n):
    swapped = False
    for a in range(0,n-1):
        for b in range(0,n-1):
            if nums[b] > nums[b+1]:
                swapped = True
                nums[b],nums[b+1] = nums[b+1], nums[b]
    return nums

nums = [5,18,22,13,70,1,7]
numsLength= len(nums)
# swapped = False

print('unsorted list: ', nums)
print('sorted list: ', bubbleSort(nums, numsLength))

t = timeit.timeit(stmt=lambda: bubbleSort(nums, numsLength), number = 1)
t=round(t,8)
print('runtime for program: {:.8f} secs using TIMEIT\n'.format(t))




