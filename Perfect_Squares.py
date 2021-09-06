from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        if sqrt(n) ** 2 == n: return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j * j)) ** 2 == n - j * j: return 2
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7: return 4
        return 3

if __name__ == '__main__':
    s = Solution()
    n = 13
    print(s.numSquares(n))
