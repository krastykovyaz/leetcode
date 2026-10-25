# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:
# Input: root = [1,2,3,4,5], subRoot = [2,4,5]
# Output: true

# Example 2:
# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
# Output: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return is_same(p.left, q.left) and is_same(p.right, q.right)
        def dfs(head):
            if not head:
                return False
            if is_same(head, subRoot):
                return True
            return dfs(head.left) or dfs(head.right)
        return dfs(root)


        


if __name__=='__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right = TreeNode(3)
    root2 = TreeNode(2)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    # root1 = TreeNode(1)
    # root1.left = TreeNode(2)
    # root1.left.left = TreeNode(4)
    # root1.left.right = TreeNode(5)
    # root1.left.left.left = TreeNode(6)
    # root1.right = TreeNode(3)
    # root2 = TreeNode(2)
    # root2.left = TreeNode(4)
    # root2.right = TreeNode(5)
    s = Solution()
    print(s.isSubtree(root1, root2))

        