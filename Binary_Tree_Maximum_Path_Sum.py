# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

# The path sum of a path is the sum of the node's values in the path.

# Example 1:
# Input: root = [1,2,3]

# Output: 6
# Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

# Example 2:
# Input: root = [-15,10,20,null,null,15,5,-5]

# Output: 40
# Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_pth = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            cur_path = node.val + left_gain + right_gain
            self.max_pth = max(self.max_pth, cur_path)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return self.max_pth

if __name__=='__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s = Solution()
    print(s.maxPathSum(root))
        