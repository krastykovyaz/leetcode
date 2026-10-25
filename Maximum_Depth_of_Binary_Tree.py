# Maximum Depth of Binary Tree
# Easy
# Topics
# Company Tags
# Hints
# Given the root of a binary tree, return its depth.

# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: 
root = [1,2,3,None,None,4]

# Output: 3
# Example 2:
# Input: 
root = []
# Output: 0
class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.right=right
        self.left=left
    
class Solution:
    def maxDepth(self, tree):
        if not tree:
            return 0
        left = self.maxDepth(tree.left)
        right = self.maxDepth(tree.right)
        return 1 + max(left, right)

if __name__=='__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    s = Solution()
    print(s.maxDepth(tree))

