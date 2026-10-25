# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.
# Example 1:
# Input: 
nums = [3,4,5,6]
target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]

def two_sum(nums, target):
    need = {}
    l = 0
    while l < len(nums):
        diff = target - nums[l]
        if nums[l] in need:
            return [need[nums[l]], l]
        need[diff] = l
        l += 1
    return []



if __name__=='__main__':
    # nums=[-1,-2,-3,-4,-5]
    # target=-8
    print(two_sum(nums, target))

