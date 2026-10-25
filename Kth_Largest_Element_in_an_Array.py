# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
# Follow-up: Can you solve it without sorting?

# Example 1:
# Input: 
# nums = [2,3,1,5,4]
# k = 2
# Output: 4

# Example 2:
# Input: 
nums = [2,3,1,1,5,5,4]
k = 3
# Output: 4
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = [-num for num in nums]
        heapq.heapify(self.nums)
        res = None
        for _ in range(k):
            res = heapq.heappop(self.nums)
        return -res

        

if __name__=='__main__':
    s = Solution()
    print(s.findKthLargest(nums, k))
    
