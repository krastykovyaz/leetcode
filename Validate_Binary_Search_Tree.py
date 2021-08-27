class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left  = left
        self.right = right

class Solution:
    def IsBynaryTree(self, root: TreeNode)-> bool:
        def help(root, lower=float('-inf'), upper=float('inf')):
            if root == None:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return help(root.left, lower, root.val) and help(root.right, root.val, upper)
        return help(root)

def make_node(temp, data):
    stack = []
    stack.append(temp)
    while len(stack):
        temp = stack[0]
        stack.pop(0)
        if not temp.left:
            if data != None:
                temp.left = TreeNode(data)
            else:
                temp.left = TreeNode()
            break
        else:
            stack.append(temp.left)
        if not temp.right:
            if data != None:
                temp.right = TreeNode(data)
            else:
                temp.right = TreeNode()
            break
        else:
            stack.append(temp.right)


def make_tree(elements):
    Tree = TreeNode(elements[0])
    for element in elements[1:]:
        make_node(Tree, element)
    return Tree

if __name__=='__main__':
    s = Solution()
    tree_list = [2, 1, 3]
    Tree = make_tree(tree_list)
    print(s.IsBynaryTree(Tree))

























