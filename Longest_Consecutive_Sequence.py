# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: 
# nums = [2,20,4,10,3,4,5]
# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:
# Input: 
nums = [0,3,2,5,4,6,1,1]
# [0,1,2,3,4,5,6]

# Output: 7
def long_seq(nums):
    nums_set = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in nums_set:
            count  = 0
            while num in nums_set:
                count += 1
                num += 1
            longest = max(longest, count)
    return longest

if __name__=="__main__":
    print(long_seq(nums))