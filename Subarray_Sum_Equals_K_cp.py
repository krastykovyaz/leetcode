from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        i = 0
        d = dict()
        d[0] = 1
        s = 0
        while i < len(nums):
            s += nums[i]
            if s - k in d:
                count += 1
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
            i += 1
        return count


if __name__ == '__main__':
    s = Solution()
    nums = [-1, -1, 1]
    k = 0
    print(s.subarraySum(nums, k))
