from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        Len = len(height) - 1
        l = 0
        area = 0
        while l < Len:
            area = max(area, min(height[l], height[Len]) * (Len - l))
            if height[l] < height[Len]:
                l += 1
            else:
                Len -= 1
        return area



if __name__ == '__main__':
    nums = [1, 2, 1]
    s = Solution()
    print(s.maxArea(nums))
