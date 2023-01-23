from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if n * 2 == len(s):
                res.append(s)
                return
            if left < n:
                dfs(left + 1, right, s + '(')
            if right < left:
                dfs(left, right + 1, s + ')')
        res = []
        dfs(0, 0, '')
        return res

if __name__=='__main__':
    s = Solution()
    n = 10
    print(s.generateParenthesis(n))