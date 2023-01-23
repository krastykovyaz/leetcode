from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 1
        nums += [-1]
        new_nums = []
        while i < len(nums):
            start = str(nums[i - 1])
            end = ''
            while i < len(nums) and nums[i] - 1 == nums[i - 1]:
                end = str(nums[i])
                i += 1

            if end != '' and end != start:
                part = '->'.join([start, end])
            else:
                part = start
            new_nums.append(part)
            i += 1
        return new_nums

if __name__=='__main__':
    obj = Solution()
    n = [0,3,8]
    print(obj.summaryRanges(n))
