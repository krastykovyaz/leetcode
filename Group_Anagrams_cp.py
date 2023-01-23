from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collector = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            collector[key].append(s)
        return sorted([v for k, v in collector.items()])


if __name__=='__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))