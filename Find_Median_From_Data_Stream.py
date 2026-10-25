# The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

# For example:

# For arr = [1,2,3], the median is 2.
# For arr = [1,2], the median is (1 + 2) / 2 = 1.5
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far.
# Example 1:

# Input:
inp = ["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

# Output:
# [null, null, 1.0, null, 2.0, null, 2.0]

# Explanation:
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.findMedian(); // return 1.0
# medianFinder.addNum(3);    // arr = [1, 3]
# medianFinder.findMedian(); // return 2.0
# medianFinder.addNum(2);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

import heapq

class MedianFinder:

    def __init__(self):
        self.l_arr = []
        self.r_arr = []    

    def rebalance(self):
        if len(self.l_arr) - len(self.r_arr) > 1:
            node = heapq.heappop(self.l_arr)
            heapq.heappush(self.r_arr, -node)
        elif len(self.r_arr) > len(self.l_arr):
            node = heapq.heappop(self.r_arr)
            heapq.heappush(self.l_arr, -node)
       

    def addNum(self, num: int) -> None:
        
        heapq.heapify(self.l_arr)
        heapq.heapify(self.r_arr)
        if self.l_arr and num < -self.l_arr[0]:
            heapq.heappush(self.l_arr, -num)
        else:
            heapq.heappush(self.r_arr, num)
        self.rebalance()
       
        
    def findMedian(self) -> float:
        if (len(self.r_arr) + len(self.l_arr)) % 2:
            return -self.l_arr[0]
        else:
            return (self.r_arr[0] + -self.l_arr[0]) / 2



if __name__=='__main__':
    mf = MedianFinder()
    # mf.addNum(1)
    # print(mf.findMedian())
    # mf.addNum(3)
    # print(mf.findMedian())
    # mf.addNum(2)
    # print(mf.findMedian())
    ["MedianFinder", "addNum", "1", "findMedian", "addNum", "2", "findMedian", "addNum", "3", "findMedian"]
    mf.addNum(1)
    print(mf.findMedian())
    

    mf.addNum(2)
    # print(mf.l_arr)
    # print(mf.r_arr)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())

        
        