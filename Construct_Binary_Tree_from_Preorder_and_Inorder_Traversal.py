# You are given two integer arrays preorder and inorder.

# preorder is the preorder traversal of a binary tree
# inorder is the inorder traversal of the same tree
# Both arrays are of the same size and consist of unique values.
# Rebuild the binary tree from the preorder and inorder traversals and return its root.

# Example 1:



# Input: 
preorder = [1,2,3,4]
inorder = [2,1,3,4]

# Output: [1,2,3,null,null,null,4]
# Example 2:

# Input: preorder = [1], inorder = [1]

# Output: [1]

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder_dict = {val : i for i,val in enumerate(inorder)}
        self.preorder_idx = 0
        def dfs(left, right):
            if left > right:
                return
            root_val = self.preorder[self.preorder_idx]
            self.preorder_idx += 1
            node = TreeNode(root_val)
            idx = self.inorder_dict[root_val]
            node.left = dfs(left, idx - 1)
            node.right = dfs(idx + 1, right)
            return node
        return dfs(0, len(inorder) - 1)

def print_bt(node):
    def dfs(node, direct, wave):
        if not node:
            return 
        print(node.val, direct, wave)
        return dfs(node.left, 'left', wave + 1) or dfs(node.right, 'right', wave + 1)
    return dfs(node, 'center', 0)

        

if __name__=='__main__':
    s = Solution()
    print_bt(s.buildTree(preorder, inorder))

        