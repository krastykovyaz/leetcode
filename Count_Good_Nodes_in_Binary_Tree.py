# Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x
# Given the root of a binary tree root, return the number of good nodes within the tree.

# Example 1:
# Input: root = [2,1,1,3,null,1,5]
# Output: 3

# Example 2:
# Input: root = [1,2,-1,3,4]
# Output: 4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, low, high):
            count = 0
            if not node:
                return count
            if low < node.val < high:
                count = 1
            count += dfs(node.left, node.val, high)
            count += dfs(node.right, low, node.val)
            return count
        return dfs(root, float('-inf'), float('inf'))




if __name__=='__main__':
    # tn = TreeNode(2)
    # tn.left = TreeNode(1)
    # tn.left.left = TreeNode(3)
    # tn.right = TreeNode(1)
    # tn.right.left = TreeNode(1)
    # tn.right.right = TreeNode(5)
    tn = TreeNode(1)
    tn.left = TreeNode(2)
    tn.left.left = TreeNode(3)
    tn.right = TreeNode(-1)
    tn.left.right = TreeNode(4)
    s = Solution()
    print(s.goodNodes(tn))


        