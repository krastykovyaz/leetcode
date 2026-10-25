# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
# Input: p = [4,7], q = [4,null,7]
# Output: false
# Example 3:
# Input: p = [1,2,3], q = [1,3,2]
# Output: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and q:
                return False
            if p and not q:
                return False
            if p.val != q.val:
                return False
            return True
        return dfs(p.left, q.left) and dfs(p.right, q.right)




if __name__=='__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    s = Solution()
    print(s.isSameTree(root1, root2))
    root1 = TreeNode(4)
    root1.left = TreeNode(7)
    root2 = TreeNode(4)
    root2.right = TreeNode(7)
    s = Solution()
    print(s.isSameTree(root1, root2))
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    s = Solution()
    print(s.isSameTree(root1, root2))
        