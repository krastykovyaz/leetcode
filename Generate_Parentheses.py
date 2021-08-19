class Solution:
    def GenParenthesis(self, n):
        if n == 0: return ['']
        anx = []
        for c in range(n):
            for left in self.GenParenthesis(c):
                for right in self.GenParenthesis(n - 1 - c):
                    anx.append(f'({left}){right}')
        return anx







if __name__=='__main__':
    n = 10
    s = Solution()
    print(len(s.GenParenthesis(n)))