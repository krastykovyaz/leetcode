from typing import List


class Solution:
    def CountOne(self, A: List[int], k: int) -> int:
        maxone = 0
        r = 0
        l = 0
        k0 = 0
        while r < len(A):
            if A[r] == 0:
                k0 += 1
            r += 1
            while k0 > k:
                if A[l] == 0:
                    k0 -= 1
                l += 1
                maxone = max(maxone, r - l)
        return maxone


if __name__ == '__main__':
    s = Solution()
    A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    K = 3
    print(s.CountOne(A, K))
