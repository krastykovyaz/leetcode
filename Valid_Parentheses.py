class Solution:
    def ParethesesIsValid(self, s: str) -> bool:
        mapping = {'}': '{', ')': '(', ']': '['}
        stack = []
        for c in s:
            if c in mapping:
                top = stack.pop() if stack else '$'
                if mapping[c] != top:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False


if __name__ == '__main__':
    sol = Solution()
    s = "[{}{}]"
    print(sol.ParethesesIsValid(s))
