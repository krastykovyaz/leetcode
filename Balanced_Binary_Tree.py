# Given a binary tree, return true if it is height-balanced and false otherwise.
# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:
# Input: 
# root = [1,2,3,null,null,4]
# Output: true
# Example 2:
# Input: root = [1,2,3,null,null,4,null,5]
# Output: false
# Example 3:
# Input: root = []
# Output: true
from typing import Optional

class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
    

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return dfs(root) != -1

if __name__=='__main__':
    # root = ListNode(1)
    # root.left = ListNode(2)
    # root.right = ListNode(3)
    # root.right.left = ListNode(4)
    root = ListNode(1)
    root.left = ListNode(2)
    root.right = ListNode(3)
    root.right.left = ListNode(4)
    root.right.left.left = ListNode(5)
    s = Solution()
    print(s.isBalanced(root))


