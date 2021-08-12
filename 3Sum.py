import timeit
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == [] or len(nums) < 3:
            return []
        triplete_list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if sorted([nums[i],nums[j],nums[k]]) not in triplete_list \
                        and i != k and j != k and i != j:
                            triplete_list.append(sorted([nums[i],nums[j],nums[k]]))
        return triplete_list
                        


if __name__=='__main__':
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(s.threeSum(nums))