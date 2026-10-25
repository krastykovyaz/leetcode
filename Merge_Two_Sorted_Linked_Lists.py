# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Input: 
list1 = [1,2,4]
list2 = [1,3,5]

# Output: [1,1,2,3,4,5]
# Example 2:

# Input: 
# list1 = []
# list2 = [1,2]

# Output: [1,2]
# Example 3:

# Input: list1 = [], list2 = []

# Output: []
from typing import Optional

class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        mlist = ListNode()
        cur = mlist
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        while l1:
            cur.next = l1
            cur = cur.next
            l1 = l1.next
        while l2:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
        
        return print_llist(mlist.next)
        
            
            

def print_llist(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next

if __name__=='__main__':

    l1 = ListNode(list1[0])
    cur = l1
    i = 1
    while i < len(list1):
        cur.next = ListNode(list1[i])
        cur = cur.next
        i += 1
    l2 = ListNode(list2[0])
    cur = l2
    i = 1
    while i < len(list2):
        cur.next = ListNode(list2[i])
        cur = cur.next
        i += 1
    # print_llist(l1)
    # print('----')
    # print_llist(l2)
    sol = Solution()
    sol.mergeTwoLists(l1, l2)
