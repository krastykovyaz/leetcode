# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

# The solution must not contain duplicate subsets. You may return the solution in any order.

# Example 1:
# Input: 
nums = [1,2,1]
# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
# Example 2:
# Input: nums = [7,7]
# Output: [[],[7], [7,7]]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        def backtrack(start, path):
            if path not in out:
                out.append(path)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack(i + 1, path + [nums[i]])
        backtrack(0, [])
        return out


if __name__=='__main__':
    s = Solution()
    print(s.subsetsWithDup(nums))
