from typing import List
class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.right = right
        self.left = left
        self.val = val

class Codec:
    def serialize(self, root: List[int])->str:
        data = []
        def preorder(root):
            if not root:
                data.append("")
                return
            data.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(data)


    def deserialize(self, data: str)->TreeNode:
        data = data.split(',')
        def preorder():
            x = data.pop(0)
            if not x:
                return None
            node = TreeNode(int(x))
            node.left = preorder()
            node.right = preorder()
            return node
        return preorder()

def create_node(temp, data):
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

def create_tree(elements):
    root = TreeNode(elements[0])
    for element in elements[1:]:
        create_node(root, element)
    return root


if __name__=='__main__':
    root = [2, 1, 3]

    s = Codec()
    d = Codec()
    Tree = create_tree(root)
    deser = d.deserialize(s.serialize(Tree))
    print(deser)
