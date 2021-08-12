from typing import List
import timeit
class Solution:
    def FindTarget(self, nums: List, target: int)->int:
        if target in nums:
            mid = len(nums) // 2
            num_1 = nums[mid]
            start = num_1 if num_1 < target else 0
            finish = num_1 if num_1 > target else len(nums)
            for i in range(start, finish):
                if nums[i] == target:
                    return i
        return -1

if __name__=='__main__':
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(s.FindTarget(nums, target))
    print(timeit.timeit(lambda : s.FindTarget(nums, target)))