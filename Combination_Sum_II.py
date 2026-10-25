# You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

# Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:

# Input: 
candidates = [9,2,2,4,6,1,5]
target = 8

# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]
# Example 2:

# Input: 
# candidates = [1,2,3,4,5]
# target = 7

# Output: [
#   [1,2,4],
#   [2,5],
#   [3,4]
# ]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []
        seen = set()
        def backtrack(start, path, remaining):
            if remaining == 0:
                out.append(path)
                return
            for i in range(start, len(candidates)):
                if start < i and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                backtrack(i + 1, path + [candidates[i]],remaining - candidates[i])
        backtrack(0, [], target)
        return out


if __name__=='__main__':
    s = Solution()
    print(s.combinationSum2(candidates, target))
