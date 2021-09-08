from typing import List
import timeit
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        calc_list = []
        for n1 in range(len(nums)):
            for n2 in range(len(nums)):                    
                for n3 in range(len(nums)):
                    if n1 != n2 and n1 != n3 and n2 != n3:
                        calc_list.append(abs(target - (n1 + n2 + n3)))
        return sorted(calc_list)[0]
        



if __name__ == '__main__':
    s = Solution()
    nums = [-1,2,1,-4]
    target = 1
    print(s.threeSumClosest(nums, target))
    print(timeit.timeit(lambda: s.threeSumClosest(nums, target)))
