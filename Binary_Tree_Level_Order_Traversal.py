# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# Example 1:
# Input: root = [1,2,3,4,5,6,7]

# Output: [[1],[2,3],[4,5,6,7]]
# Example 2:

# Input: root = [1]

# Output: [[1]]
# Example 3:

# Input: root = []

# Output: []

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.nodes = []
        def dfs(root_, level):
            if not root_:
                return
            if len(self.nodes) == level:   
                self.nodes.append([])
            print(level, self.nodes)
            self.nodes[level].append(root_.val)
            dfs(root_.left, level + 1)
            dfs(root_.right, level + 1) 
            
        dfs(root, 0)
        return self.nodes


if __name__=='__main__':
    tn = TreeNode(1)
    tn.left = TreeNode(2)
    tn.left.left = TreeNode(4)
    tn.left.right = TreeNode(5)
    tn.right = TreeNode(3)
    tn.right.right = TreeNode(7)
    tn.right.left = TreeNode(6)
    s = Solution()
    print(s.levelOrder(tn))

        