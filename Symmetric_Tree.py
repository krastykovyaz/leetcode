class NodeTree():
    def __init__(self, val=0, left=None, right=None):
        self.right = right
        self.left = left
        self.val = val

class Solution:
    def IsSymmetric(self, root: NodeTree)-> bool:
        return self.IsMirror(root, root)

    def IsMirror(self, r1, r2):
        if r1 is None and r2 is None:
            return True
        if r1 is not None and r2 is not None:
            if r1.val == r2.val:
              return self.IsMirror(r1.left, r2.right) and self.IsMirror(r1.right, r2.left)
        return False


def gen_nodes(temp, data):
    stack = []
    stack.append(temp)
    while len(stack):
        temp = stack[0]
        stack.pop(0)
        if not temp.left:
            if data != None:
                temp.left = NodeTree(data)
            else:
                temp.left = NodeTree()
            break
        else:
            stack.append(temp.left)
        if not temp.right:
            if data != None:
                temp.right = NodeTree(data)
            else:
                temp.right = NodeTree()
            break
        else:
            stack.append(temp.right)


def make_tree(elements):
    Tree = NodeTree(elements[0])
    for element in elements[1:]:
        gen_nodes(Tree, element)
    return Tree


if __name__ == '__main__':
    s = Solution()
    tree_list = [1,2,2,3,4,4,3]
    Tree = make_tree(tree_list)
    print(s.IsSymmetric(Tree))
