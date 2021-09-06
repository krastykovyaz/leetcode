from typing import List
import collections


class Solution:
    def DivisionK(self, A: List[int], K: int) -> int:
        stack = [0]
        for a in A:
            stack.append((stack[-1] + a) % K)
        count = collections.Counter(stack)
        return sum(v * (v-1) / 2 for v in count.values())


if __name__ == '__main__':
    a = [4, 5, 0, -2, -3, 1]
    k = 5
    s = Solution()
    print(s.DivisionK(a, k))
