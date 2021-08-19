import timeit


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or s == s[::-1]:
            return s
        start, maxlen = 0, 1
        for i in range(1, len(s)):
            odd = s[maxlen-i - 1:i + 1]
            even = s[maxlen-i:i+1]
            if odd == odd[::-1] and maxlen - i -1 >=0:
                start = maxlen - i -1
                maxlen += 2
            if even == even[::-1] and maxlen -1 >=0:
                start = maxlen -1
                maxlen += 1
        return s[start:start + maxlen]



if __name__ == '__main__':
    sol = Solution()
    s = "abacdfgdcaba"
    print(sol.longestPalindrome(s))
    print(timeit.timeit(lambda: sol.longestPalindrome(s), number=1))
