##################################
# insertion sort algorithm
# big O notation : O(n^2)
# space complexity: O(1)
# runtime using timeit: 0.00001870 
##################################


import timeit, random

def insertionSort(nums, current_index):
    for i in range(1, len(nums)): 
        key = nums[i]
        j = i-1
        # if key < nums[j]: 
        #     nums[j+1] = nums[j]
        #     j = j - 1
        # if key > nums[j]: 
        #     break
        while j >= 0 and key < nums[j]:
            nums[j+1]  = nums[j] 
            j = j - 1
        nums[j+1] = key


nums= [5,18,22,13,70,1,7] 
current_index = nums[1]
print('unsorted list: ', nums)
insertionSort(nums, current_index)
print('sorted list using insertion: ', nums)

# t = timeit.timeit(stmt=lambda: insertionSort(nums, current_index), number = 1)
# t=round(t,8)
# print('runtime for selection sort: {:.8f} secs using TIMEIT\n'.format(t))


#recursive selection sort
def insertionSort(nums, current_index):
    if len(nums) == 0:
        return 0
    else: 
        for i in range(1,len(nums)):
            key= nums[i] 
            j = i-1
            if j >= 0 and key<nums[j]:
                nums[j+1]  = nums[j] 
                insertionSort(j-1)
            nums[j+1] = key
                

nums = [5,18,22,13,70,1,7]
current_index = nums[1]