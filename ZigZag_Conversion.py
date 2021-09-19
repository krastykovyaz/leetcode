class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lst = [""] * numRows
        i = 0
        up = False
        for c in s:
            lst[i] += c
            if up:
                if i == 0:
                    i += 1
                    up = True
                else:
                    i -= 1
            else:
                if i == numRows - 1:
                    i -= 1
                    up = False
                else:
                    i += 1
        return "".join(lst)


if __name__ == '__main__':
    s = Solution()
    string = '''P   A   H   N
                A P L S I I G
                Y   I   R'''
    num = 3
    print(s.convert(string, num))
