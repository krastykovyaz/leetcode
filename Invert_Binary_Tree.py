# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Example 1:
# Input: 
root = [1,2,3,4,5,6,7]
# Output: [1,3,2,7,6,5,4]

# Example 2:
# Input: root = [3,2,1]
# Output: [3,1,2]

# Example 3:
# Input: root = []
# Output: []

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.right = right
        self.left = left
        self.val = val

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right,  root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        

def print_bt(root):
    print(root.val)


if __name__=='__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.right = TreeNode(5)
    tree.left.left.left = TreeNode(6)
    tree.right.right.right = TreeNode(7)
    s = Solution()
    s.invertTree(tree)
    print_bt(tree)
    print_bt(tree.left)
    print_bt(tree.right)
    print_bt(tree.left.left)
    print_bt(tree.right.right)
    print_bt(tree.left.left.left)
    print_bt(tree.right.right.right)

        
            