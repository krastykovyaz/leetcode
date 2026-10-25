# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.
# A binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.
# Example 1:

# Input: root = [2,1,3], k = 1
# Output: 1
# Example 2:

# Input: root = [4,3,5,2,null], k = 4
# Output: 5

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.count = 0
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.count += 1
            if self.count == k:
                self.res = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.res

if __name__=='__main__':
    # tn = TreeNode(2)
    # tn.left = TreeNode(1)
    # tn.right = TreeNode(3)
    # k = 1
    tn = TreeNode(4)
    tn.left = TreeNode(3)
    tn.left.left = TreeNode(2)
    tn.right = TreeNode(5)
    k = 4
    s = Solution()
    print(s.kthSmallest(tn, k))
        