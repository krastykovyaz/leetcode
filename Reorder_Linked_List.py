# You are given the head of a singly linked-list.
# The positions of a linked list of length = 7 for example, can intially be represented as:
head = [0, 1, 2, 3, 4, 5, 6]
# Reorder the nodes of the linked list to be in the following order:
# [0, 6, 1, 5, 2, 4, 3]
# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
# [0, n-1, 1, n-2, 2, n-3, ...]
# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def reorderList(self, head_: Optional[ListNode]) -> None:
        slow = head_
        fast = head_
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        second = self.reverse(second)
        first = head_
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        print_ll(head_)

    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        return prev

def print_ll(ll):
    cur = ll
    while cur:
        print(cur.val)
        cur = cur.next

if __name__=='__main__':
    root = ListNode(head[0])
    cur = root
    i = 1
    while i < len(head):
        cur.next = ListNode(head[i])
        cur = cur.next
        i += 1
    # print_ll(root)
    s = Solution()
    print_ll(s.reorderList(root))
    # s.reverse(root)
    

