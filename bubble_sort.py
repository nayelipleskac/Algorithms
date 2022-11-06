#Bubble Sort

import timeit, random, big_o

#############################
## bubble sort algorithm
## runtime & time complexity:
## O(n^2): 2 nested for loops
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
# nums = [5,18,22,13,70,1,7,23,5,6,90,54,19,1,0,67]
# nums = [5,18,22,13,70,1,7,23,5,6,90,54,19,1,0,67,80,63,17,300,193,9384,823,4,95,98,288,234,4829,34,78]
numsLength= len(nums)
# swapped = False
print('length of list', numsLength)
print('unsorted list: ', nums)
print('sorted list: ', bubbleSort(nums, numsLength))

t = timeit.timeit(stmt=lambda: bubbleSort(nums, numsLength), number = 1)
t=round(t,8)
print('runtime for program: {:.8f} secs using TIMEIT\n'.format(t))





