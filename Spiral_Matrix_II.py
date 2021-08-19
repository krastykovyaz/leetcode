from typing import List
class Solution:
    def GenSpiral(self, n: int)-> List[List[int]]:
        if not n:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]
        top, down,left, right, num = 0, n-1, 0, n-1, 1
        while top <= down and left <= right:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1
            for i in range(top, down + 1):
                res[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                res[down][i] = num
                num += 1
            down -= 1
            for i in range(down, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res




if __name__=='__main__':
    s = Solution()
    n = 3
    print(s.GenSpiral(n))