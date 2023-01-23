from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        agg = {}
        while i < len(nums):
            k = target - nums[i]
            if k in agg:
                return [agg[k], i]
            agg[nums[i]] = i
            i += 1





if __name__=='__main__':
    s = Solution()
    nums = [3,3]
    t = 6
    print(s.twoSum(nums, t))