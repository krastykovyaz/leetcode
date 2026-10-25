# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O(n)
# O(n) time without using the division operation?

# Example 1:

# Input: 
nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: 
# nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]

def dot_product(nums):
    n = len(nums)
    out = [1] * n
    left = 1            # 0 round left [1,1,1,1]
    for i in range(n):      # 1 round left [1,2*1,2*1*4,1]
        out[i] = left # 2 round left [1,2*1,2*1*4,1]
        left *= nums[i]           # 3 round left [1,1*2,1*2*4,1*2*4]
    right = 1                       # 0 round right [1,2,8,8]
    for j in range(n - 1, -1, -1): # 1 round right [1,2,8,8*1]
        out[j] *= right        # 2 round right [1,2,8*4,8*1]
        right *= nums[j]                  # 3 round right [1,2*4*2,8*4,8*1]
    return out                         # fin round right [1*2*4*6,2*4*2,8*4,8*1]       
                                        # output [48,16,32,8]

if __name__=='__main__':
    print(dot_product(nums))