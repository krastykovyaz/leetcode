from typing import List


class Solution:
    def IsOnLine(self, points: List[List[int]]) -> True:
        if not points:
            return True
        mX = max(points, key = lambda x:x[0])[0] + min(points, key = lambda x:x[0])[0]
        m = mX / 2.0
        right = set()
        reflected = set()
        for x, y in points:
            if x > m:
                right.add((x, y))
            elif x < m:
                reflected.add((mX - x, y))
        return right == reflected


if __name__ == '__main__':
    points = [[1, 1], [-1, -1]]
    s = Solution()
    print(s.IsOnLine(points))
