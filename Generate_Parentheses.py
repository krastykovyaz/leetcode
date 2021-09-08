from typing import List
class Solution:
    def GenParenthesis(self, n: int)->List[str]:
        if n == 0: return['']
        ans = []
        for c in range(n):
            for left in self.GenParenthesis(c):
                for right in self.GenParenthesis(n -c -1):
                    ans.append(f"({left}){right}")
        return ans



if __name__=='__main__':
    n = 5
    s = Solution()
    print(s.GenParenthesis(n))