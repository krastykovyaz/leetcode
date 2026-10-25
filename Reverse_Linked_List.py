# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:
# Input: 
head = [0,1,2,3]
# Output: [3,2,1,0]

# Example 2:
# Input: head = []
# Output: []

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    while cur:
        next_ = cur.next
        cur.next = prev
        prev = cur
        cur = next_
    print_linked_list(prev)

def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next


if __name__=='__main__':
    node = ListNode(head[0])
    cur = node
    i = 1
    while i < len(head):
        cur.next = ListNode(head[i])
        cur = cur.next
        i += 1
    reverseList(node)

