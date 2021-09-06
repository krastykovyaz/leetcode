from typing import List


class Solution:
    def GetLenNonZero(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        res = 0
        l = len(nums)
        for n in nums:
            if n != 0:
                curr += 1
            else:
                res = max(res, prev + curr)
                prev = curr
                curr = 0
        return max(res, prev+curr) - 1 if l == curr else max(res, prev+curr)


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,0,1]
    print(s.GetLenNonZero(nums))