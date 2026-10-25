# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution must run in 
# O(log(m+n))
# O(log(m+n)) time.

# Example 1:

# Input: 
nums1 = [1,2]
nums2 = [3]

# Output: 2.0
# Explanation: Among [1, 2, 3] the median is 2.

# Example 2:

# Input: 
nums1 = [1,3]
nums2 = [2,4]

# Output: 2.5
# Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5

from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left = 0
    right = m
    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i
        left1 = nums1[i - 1] if i > 0 else float('-inf')
        right1 = nums1[i] if i < m else float('inf')
        left2 = nums2[j - 1] if j > 0 else float('-inf')
        right2 = nums2[j] if j < n else float('inf')
        if left1 <= right2 and left2 <= right1:
            if (n + m) % 2 == 1:
                return max(left1, left2)
            else:
                return (max(left1,left2) + min(right1, right2)) / 2
        elif left1 > right2:
            right = i - 1
        else:
            left = i + 1





if __name__=='__main__':
    print(findMedianSortedArrays(nums1, nums2))
