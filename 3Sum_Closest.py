from typing import List
import timeit
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        calc_list = []
        result = {}
        for n1 in range(len(nums)):
            for n2 in range(len(nums)):
                for n3 in range(len(nums)):
                    if n1 != n2 and n1 != n3 and n2 != n3:
                        minimum = abs(target - (nums[n1] + nums[n2] + nums[n3]))
                        result[minimum] = nums[n1] + nums[n2] + nums[n3]
                        calc_list.append(minimum)
        return result[sorted(calc_list)[0]]
        



if __name__ == '__main__':
    s = Solution()
    nums = [-43,61,-62,24,73,64,-23,94,-65,-27,24,-56,8,54,0,19,-100,-64,-53,6,-22,13,-18,55,-41,37,34,-43,0,-8,-95,76,73,21,-93,16,98,60,70,-32,30,-7,-27,-73,79,-26,41,32,41,-5,82,-14,50,-94,22,62,60,-48,51,12,-34,68,-40,-20,-20,46,46,-79,1,82,-98,41,-79,-43,-76,-25,-94,-16,-25,46,-95,-79,53,-1,-30,43,93,17,72,66,83,-89,-16,42,40,87,-46,40,22,85,-91,46,-77,19,-56,-28,8,47,-20,65,8,60,-49,-86,-74,56,30,79,97,-89,14,-90,66,-12,-57,46,-61,87,72,13,75,75,36,79,-16,84,-49,-86,76,68,-8,-65,-86,-11,55,-69,-59,34,63,59,-11,43,16,7,93,57,-55,2,38,64,3,22,-9,-22,-34,-84,90,-71,-88,64,-19,13,-8,-81,-95,-38,-9,-25,82,57,60,-26,66,21,8,65,-38,-68,-59,24,91,-231]
    target = 1
    print(s.threeSumClosest(nums, target))
    print(timeit.timeit(lambda: s.threeSumClosest(nums, target)))
