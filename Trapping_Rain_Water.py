from typing import List
class Solution:
    def FillWater(self, height: List[int])->int:
        length = len(height) - 1
        start = 0
        maxr, maxl, water = 0,0,0
        while start < length:
            if height[start] < height[length]:
                if maxl < height[start]:
                    maxl = height[start]
                else:
                    water += maxl - height[start]
                start += 1
            else:
                if maxr < height[length]:
                    maxr = height[length]
                else:
                    water += maxr - height[length]
                length -= 1
        return water




if __name__ == '__main__':
    s = Solution()
    height = [4,2,0,3,2,5]
    print(s.FillWater(height))