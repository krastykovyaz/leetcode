from collections import defaultdict
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        symbols = defaultdict(int)
        for c in chars:
            symbols[c] += 1
        res = ''.join([str(s) for t in list(symbols.items()) for s in t if s != 1])
        return len(res)

if __name__=='__main__':
    s = Solution()
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(s.compress(chars))
