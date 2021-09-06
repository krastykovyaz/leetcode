from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        res = 0
        for n in nums:
            if n == 1:
                curr += 1
            else:
                res = max(res, curr + prev)
                prev = curr + 1
                curr = 0
        return max(res, curr + prev)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, 1, 1, 1, 0]
    print(s.findMaxConsecutiveOnes(nums))
