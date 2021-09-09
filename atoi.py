class Solution:
    def myAtoi(self, s: str) -> int:
        if s:
            i = 0
            f = 0
            while s[i] == ' ':
                i += 1
                if len(s) == i:
                    return 0
            neg = 0

            if s[i] == '-':
                neg = 1
                i += 1
            if not neg:
                if s[i] == '+':
                    i += 1
            num = ''
            while i < len(s):
                if s[i] not in '0987654321':
                    break
                num += s[i]
                f = 1
                i += 1
            if f:
                if neg: num = '-' + num
                if -2147483648 > int(num):
                    return -2147483648
                if 2147483647 < int(num):
                    return 2147483647
                return int(num)
            return 0


if __name__ == '__main__':
    s = Solution()
    string = " "
    print(s.myAtoi(string))