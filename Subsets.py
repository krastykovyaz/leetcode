# Given an array nums of unique integers, return all possible subsets of nums.

# The solution set must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: 
nums = [1,2,3]

# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: 
# nums = [7]

# Output: [[],[7]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.out = []
        def backtrack(start, path):
            self.out.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        backtrack(0,[])
        return self.out


if __name__=='__main__':
    s = Solution()
    print(s.subsets(nums))
