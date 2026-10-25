# Generate Parentheses
# Medium
# Topics
# Company Tags
# Hints
# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# Example 1:

# Input: n = 1

# Output: ["()"]
# Example 2:

# Input: 
n = 3

# Output: ["((()))","(()())","(())()","()(())","()()()"]
# You may return the answer in any order.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        def backtrack(path, l, r):
            # print(path)
            if len(path) == n * 2:
                out.append(path)
                return
            if l < n:
                backtrack(path + '(', l + 1, r)
            if l > r:
                backtrack( path + ')', l, r + 1)
        backtrack('',0,0)
        return out

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(n))

