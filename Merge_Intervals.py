from typing import List

class Solution:
    def Merge(self,intervals: List[List[int]])->List:
        merged_list = []
        for i in range(len(intervals)):
            if i > 0:
                if intervals[i][0] <= intervals[i - 1][1]:
                    merged_list.append([intervals[i - 1][0], intervals[i][1]])
                else:
                    merged_list.append([intervals[i][0], intervals[i][1]])
        return merged_list


if __name__=='__main__':
    s = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(s.Merge(intervals))