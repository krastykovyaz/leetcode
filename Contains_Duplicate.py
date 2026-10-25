# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:
# Input: 
# nums = [1, 2, 3, 3]
# Output: true

# Example 2:
# Input: 
nums = [1, 2, 3, 4]
# Output: false

def is_duplic(arr):
    storage = {}
    for ar in arr:
        if ar not in storage:
            storage[ar] = 1
        else:
            return 'true'
    return 'false'

if __name__=='__main__':
    print(is_duplic(nums))