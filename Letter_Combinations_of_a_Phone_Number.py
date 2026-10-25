# You are given a string digits made up of digits from 2 through 9 inclusive.

# Each digit (not including 1) is mapped to a set of characters as shown below:

# A digit could represent any one of the characters it maps to.

# Return all possible letter combinations that digits could represent. You may return the answer in any order.

# Example 1:
# Input: 
digits = "34"
# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
# Example 2:
# Input: digits = ""
# Output: []

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = {2:'ABC',
                    3: 'DEF',
                    4: 'GHI',
                    5: 'JKL',
                    6: 'MNO',
                    7: 'PQRS',
                    8: 'TUV',
                    9: 'WXYZ'}
        out = []
        def backtrack(path, idx):
            if len(path) == len(digits):
                out.append(path)
                return
            mapp =  digit_map[int(digits[idx])]
            for ch in mapp:
                backtrack(path + ch.lower(), idx+1)
        backtrack('',0)
        return out

        
        

if __name__=='__main__':
    s = Solution()
    print(s.letterCombinations(digits))