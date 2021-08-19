from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m < len(nums1):
            if nums1[m] == 0:
                nums1[m] += nums2[n - 1]
                n -= 1
            m += 1
        return sorted(nums1)


if __name__=='__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(s.merge(nums1,  m, nums2, n))