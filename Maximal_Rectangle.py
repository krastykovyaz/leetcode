from typing import List
class Solution:
    def FindRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or matrix == [[0]]:
            return 0
        n = len(matrix[0])
        height = (n + 1) * [0]
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(1 + n):
                while height[i] < height[stack[-1]]:
                    pop = stack.pop()
                    h = height[pop]
                    w = i - 1 - stack[-1]
                    ans = max(ans, w * h)
                stack.append(i)
        return ans


if __name__=='__main__':
    s = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(s.FindRectangle(matrix))

