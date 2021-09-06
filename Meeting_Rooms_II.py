from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[int])->int:
        intervals = sorted(intervals,key=lambda x: x[0])
        min_heap = []
        for interval in intervals:
            if not min_heap or min_heap[0] > interval[0]:
                heapq.heappush(min_heap, interval[1])
            else:
                heapq.heapreplace(min_heap, interval[1])
        return len(min_heap)


if __name__=='__main__':
    s = Solution()
    intervals = [[1,30],[2,15],[20,25]]
    print(s.minMeetingRooms(intervals))