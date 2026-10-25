# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

# The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

# Given the root of a binary tree root, return the diameter of the tree.

# Example 1:



# Input: 
root = [1,None,2,3,4,5]

# Output: 3
# Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

# Example 2:

# Input: 
# root = [1,2,3]

# Output: 2
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.diameter

if __name__=='__main__':
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(4)
    tree.right.left.left = TreeNode(5)
    s = Solution()
    print(s.diameterOfBinaryTree(tree))
        
