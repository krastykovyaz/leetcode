# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

# You may return the solution in any order.

# Example 1:

# Input: 
s = "aab"

# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: 
# s = "a"

# Output: [["a"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        path = []
        def backtrack(start):
            if len(s) == start:
                out.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if s[start:end] == s[start:end][::-1]:
                    path.append(s[start:end])
                    backtrack(end)
                    path.pop()
        backtrack(0)
        return out





if __name__=='__main__':
    sol = Solution()
    print(sol.partition(s))