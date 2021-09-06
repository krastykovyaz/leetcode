from typing import List


class Solution:
    def ProductExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        for i in range(1, len(nums)):
            out[i] = out[i - 1] * nums[i - 1]
        ml = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * ml
            ml = nums[i] * ml
        return out


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    s = Solution()
    print(s.ProductExceptSelf(nums))
