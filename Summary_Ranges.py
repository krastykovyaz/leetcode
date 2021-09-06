from typing import List
class Solution:
    def SumRan(self, nums: List[int])-> List[int]:
        tmp_list = []
        result_list = []
        if nums == []:
            return []
        if nums == [-1]:
            return [-1]
        for i in range(len(nums)):
            if i + 1 < len(nums):
                if nums[i + 1] - nums[i] == 1:
                    tmp_list.append(nums[i])
                else:
                    tmp_list.append(nums[i])
                    if len(tmp_list) > 0 and tmp_list[0] != tmp_list[-1]:
                        result_list.append(f"{tmp_list[0]}->{tmp_list[-1]}")
                    else:
                        result_list.append(f"{tmp_list[0]}")
                    tmp_list = []
        else:
            if len(tmp_list) == 0:
                result_list.append(f"{nums[i]}")
            else:
                result_list.append(f"{tmp_list[0]}->{nums[i]}")
        return result_list


if __name__=='__main__':
    s = Solution()
    nums = [0,1,2,4,5,7]
    print(s.SumRan(nums))
