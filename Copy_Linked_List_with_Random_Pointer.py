# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

# Create a deep copy of the list.

# The deep copy should consist of exactly n new nodes, each including:

# The original value val of the copied node
# A next pointer to the new node corresponding to the next pointer of the original node
# A random pointer to the new node corresponding to the random pointer of the original node
# Note: None of the pointers in the new list should point to nodes in the original list.

# Return the head of the copied linked list.

# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Example 1:

# Input: 
head = [[3,None],[7,3],[4,0],[5,1]]

# Output: 
# [[3,null],[7,3],[4,0],[5,1]]

# Input: head = [[1,null],[2,2],[3,2]]
# Output: [[1,null],[2,2],[3,2]]
from typing import Optional

class Node:
    def __init__(self, val = 0, next_: 'Node' = None, random = None):
        self.val = val
        self.next = next_
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        mapping = {}
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            mapping[cur].next = mapping.get(cur.next)
            mapping[cur].random = mapping.get(cur.random)
            cur = cur.next
        print_ll(mapping)
        return mapping[head]
        

def print_node(root):
    cur = root
    if cur is not None:
        return cur.val
    return cur

def print_ll(head):
    i = 0
    while i < len(head):
        cur = list(head)[i]
        print('index:', i)
        print('val:', cur.val)
        print('next point:', print_node(cur.next))
        print('rand point:', print_node(cur.random))
        print('-------')
        i += 1

if __name__=='__main__':
    head_lst = [Node(item) for item in head]
    for i, (nxt, rand) in enumerate(head):
        if i + 1 < len(head):
            head_lst[i].next = head_lst[i + 1]
        if rand is not None:
            head_lst[i].random = head_lst[rand]
    head_ = head_lst[0]
    s = Solution()
    s.copyRandomList(head_)