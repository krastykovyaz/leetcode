from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        print(num)
        if len(num) % 2 == 0:
            return (num[len(num) // 2 - 1] + num[len(num) // 2]) / 2
        else:
            return format(float(num[int(len(num) / 2)]), '5f')



if __name__=='__main__':
    s = Solution()
    nums1 = [1,3]
    nums2 = [2]
    print(s.findMedianSortedArrays(nums1, nums2))