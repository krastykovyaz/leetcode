# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.
# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

# Example 1:
# Input: 
# root = [5,3,8,1,4,7,9,None,2]
p = 3
q = 8
# Output: 5
# Example 2:
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
# Output: 3

# from typing import
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root.val

        
        
    

if __name__=='__main__':
    tn = TreeNode(5)
    tn.left = TreeNode(3)
    tn.left.left = TreeNode(1)
    tn.left.left.right = TreeNode(2)
    tn.left.right = TreeNode(4)
    tn.right = TreeNode(8)
    tn.right.right = TreeNode(9)
    tn.right.left = TreeNode(7)
    p = TreeNode(3)
    q = TreeNode(4)
    s = Solution()
    print(s.lowestCommonAncestor(tn, p, q))




