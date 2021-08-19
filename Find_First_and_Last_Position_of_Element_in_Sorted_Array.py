from typing import List
class Solution:
    def FindIndexes(self, nums: List[int], target: int)-> List:
        mid = len(nums) // 2
        start = mid if mid < target else 0
        finish = mid if mid > target else len(nums)
        returned_start = 0
        if target in nums:
            while start < finish:
                i = 0
                while nums[start] == target:
                    returned_start = start
                    i += 1
                    start += 1
                else:
                    start += 1
            returned_finish = returned_start - i + 1
            return [returned_finish, returned_start]
        else:
            return [-1, -1]

if __name__=='__main__':
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 0
    print(s.FindIndexes(nums, target))