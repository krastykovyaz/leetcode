# Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

# Implement the following methods:

# constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
# int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
# Example 1:

# Input:
# ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

# Output:
# [null, 3, 3, 3, 5, 6]

# Explanation:
# KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
# kthLargest.add(3);   // return 3
# kthLargest.add(5);   // return 3
# kthLargest.add(6);   // return 3
# kthLargest.add(7);   // return 5
# kthLargest.add(8);   // return 6


# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.heap = []
#         self.k = k
#         for num in nums:
#             self.add(num)
        

#     def add(self, val: int) -> int:
#         if len(self.heap) < self.k:
#             self.push(val)
#         if self.heap[0] < val:
#             self.heap[0] = val
#             self.heapify_down(0)
#         return self.heap[0]

#     def push(self, val):
#         self.heap.append(val)
#         self.heapify_up(len(self.heap) -  1)

#     def heapify_up(self, i):
#         parent = (i - 1) // 2
#         while i > 0 and self.heap[i] < self.heap[parent]:
#             self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
#             i = parent
#             parent = (i - 1) // 2

#     def heapify_down(self, i):
#         n = len(self.heap)
#         while True:
#             smallest = i
#             left = 2 * i + 1
#             right = i * 2 + 2
#             if left < n and self.heap[smallest] > self.heap[left]:
#                 smallest = left
#             if right < n and self.heap[smallest] > self.heap[right]:
#                 smallest = right
#             if i == smallest:
#                 break
#             self.heap[i], self.heap[smallest] = self.heap[smallest] , self.heap[i]
#             i = smallest
import heapq
            
class KthLargest:
    def __init__(self, k, lst):
        self.k = k
        self.nums = lst
        heapq.heapify(self.nums)
        while self.k < len(self.nums):
            heapq.heappop(self.nums)



        
    def add(self, val):
        heapq.heappush(self.nums, val)
        if self.k < len(self.nums):
            heapq.heappop(self.nums)
        return self.nums[0]




                

if __name__=='__main__':
    lst = [1, 2, 3, 3]
    k = 3
    k_l = KthLargest(k, lst)
    print(k_l.add(3))
    print(k_l.add(5))
    print(k_l.add(6))
    print(k_l.add(7))
    print(k_l.add(8))

        
