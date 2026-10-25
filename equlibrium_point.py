# Given an array of integers arr[], the task is to find the first equilibrium point in the array.

# The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

# Examples:

# Input: 
# arr = [1, 2, 0, 3]
# Output: 2 
# Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
# Input: 
# arr = [1, 1, 1, 1]
# Output: -1
# Explanation: There is no equilibrium index in the array.
# Input: 
arr = [-7, 1, 5, 2, -4, 3, 0]
# Output: 3
# Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1

def find_eqilibrium(arr):
    total = sum(arr)
    left_total = 0
    i = 0
    while i < len(arr):
        total -= arr[i]
        if total == left_total:
            return i
        left_total += arr[i]
        i += 1
    return -1


if __name__=='__main__':
    print(find_eqilibrium(arr))