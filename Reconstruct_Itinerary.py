from collections import defaultdict
from typing import List


class Solution:
    def SortTickets(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for src, dest in tickets:
            d[src].append(dest)
        for key, value in d.items():
            d[key] = sorted(value, reverse=True)
        stack = ['JFK']
        result = []
        while stack:
            ret = stack[-1]
            if ret in d and d[ret]:
                stack.append(d[ret].pop())
            else:
                result.append(stack.pop())
        return result[::-1]


if __name__ == '__main__':
    inp = [["MUC", "LHR"],
           ["JFK", "MUC"],
           ["SFO", "SJC"],
           ["LHR", "SFO"]]
    s = Solution()
    print(s.SortTickets(inp))
