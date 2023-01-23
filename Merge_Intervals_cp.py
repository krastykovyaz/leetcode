from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        # if len(intervals) == 1:
        #     return intervals
        res = self._get_inter(intervals, [])
        return res

    def _get_inter(self, seq, res):

        for s in seq:
            if not res or s[0] > res[-1][1]:
                res.append(s)
            elif s[0] <= res[-1][1]:
                res[-1] = [min(s[0], res[-1][0]), max(s[1], res[-1][1])]
        if len(seq) > len(res):
            res = self._get_inter(res, [])
        return res


if __name__ == '__main__':
    inter = [[1, 3],[4,5]]
    s = Solution()
    print(s.merge(inter))
