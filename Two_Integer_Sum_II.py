# Two Integer Sum II
# Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
# There will always be exactly one valid solution.

# Your solution must use O(1) additional space.

# Example 1:
# Input: 
numbers = [1,2,3,4]
target = 3
# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

def two_int_sum(nums, k):
    r =len(nums) - 1
    l = 0
    while l < r:
        if nums[l] + nums[r] == k:
            return [l+1, r+1]
        if nums[l] + nums[r] > k:
            r -= 1
        else:
            l += 1
    return []




if __name__=='__main__':
    numbers=[-5,-3,0,2,4,6,8]
    target=5
    # output [7,2]
    print(two_int_sum(numbers, target))