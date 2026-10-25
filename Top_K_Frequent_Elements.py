# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Example 1:
# Input: 
nums = [1,2,2,3,3,3]
k = 2

# Output: [2,3]
# Example 2:

# Input: 
# nums = [7,7]
# k = 1

# Output: [7]

def top_k_element(nums,k):
    import heapq
    from collections import Counter
    freq = Counter(nums)
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [item[1] for item in heap]

if __name__=='__main__':
    print(top_k_element(nums, k))