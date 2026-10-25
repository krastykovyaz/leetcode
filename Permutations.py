# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

# Example 1:

# Input: 
nums = [1,2,3]

# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [7]

# Output: [[7]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        is_seen = [0] * len(nums)
        def backtrack(path):
            if len(path) == len(nums) :
                out.append(path)
                return
            for i in range(len(nums)):
                if is_seen[i] == 1:
                    continue
                is_seen[i] = 1
                backtrack(path + [nums[i]])
                is_seen[i] = 0
       

        backtrack([])
        return out

if __name__ == '__main__':
    s = Solution()
    print(s.permute(nums))