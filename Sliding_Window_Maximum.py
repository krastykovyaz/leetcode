# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

# Example 1:

# Input: 
nums = [1,2,1,0,4,2,6]
k = 3

# Output: [2,2,4,4,6]

# Explanation: 
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6


from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    if not nums:
        return []
    out = []
    prev_step = 0

    for step in range(len(nums) - k + 1):
        out.append(max(nums[step:step + k]))
    return out

if __name__=='__main__':
    nums=[1,-1]
    k=1
    print(maxSlidingWindow(nums, k))
