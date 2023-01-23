from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count += 1
                i -= 1
            i += 1
            print(nums)
        nums.extend(count * [0])
        return nums

if __name__=='__main__':
    s = Solution()
    nums = [0,0,1]
    print(s.moveZeroes(nums))
