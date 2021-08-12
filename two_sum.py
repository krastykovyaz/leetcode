from typing import List
import timeit

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        return []


if __name__=='__main__':
    nums = [3,3]
    target = 6
    s = Solution()
    print(s.twoSum(nums,target))
    print(timeit.timeit(lambda: s.twoSum(nums,target), number=1))
