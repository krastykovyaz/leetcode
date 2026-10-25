# You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,4,null,5]
# Output: [1,3,5]
# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]
# Example 3:
# Input: root = [1,null,2]
# Output: [1,2]
# Example 4:
# Input: root = []
# Output: []

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

            

if __name__=='__main__':
    # [1,2,3,null,4,null,5]
    tn = TreeNode(1)
    tn.left = TreeNode(2)
    tn.right = TreeNode(3)
    tn.right.right = TreeNode(4)
    tn.right.right.right = TreeNode(5)
    s = Solution()
    print(s.rightSideView(tn))
        