# Implement an algorithm to serialize and deserialize a binary tree.

# Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

# Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.

# Example 1:



# Input: 
# root = [1,2,3,null,null,4,5]

# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []

# Output: []

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.out = []
        def dfs(node):
            if not node:
                self.out.append('null')
                return
            self.out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ', '.join(self.out)




        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        self.data = data.split(', ')
        self.idx = 1
        def dfs():
            if self.data[self.idx] == 'null':
                self.idx += 1
                return
            node = TreeNode(int(self.data[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return root
        return print_bt(dfs())

def print_bt(root):
    def dfs(node):
        if not node:
            return
        print(node.val)
        print_bt(node.left)
        print_bt(node.right)
    dfs(root)
    



if __name__=='__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    c = Codec()
    print(c.serialize(root))
    print(c.deserialize(c.serialize(root)))