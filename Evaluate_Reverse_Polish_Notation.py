from typing import List

class Solution:
    def calculator(self, tokens: List[int])->int:

        def operations(sign, n1, n2):
            if sign == '*':
                return n1 * n2
            elif sign == '+':
                return n1 + n2
            elif sign == '-':
                return n2 - n1
            else:
                return int(n2 / n1)

        nums = []
        for token in tokens:
            if token not in "+-*/":
                nums.append(int(token))
            else:
                nums.append(operations(token, nums.pop(), nums.pop()))
        return nums[-1]



if __name__=='__main__':
    nums = ["4", "13", "5", "/", "+"]
    s = Solution()
    print(s.calculator(nums))