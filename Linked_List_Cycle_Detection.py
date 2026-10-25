# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

# Note: index is not given to you as a parameter.
from typing import Optional
# Input: 
# head = [1,2,3,4]
# index = 1

# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
head = [1,2]
index = -1

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     storage = set()
    #     cur = head
    #     while cur:
    #         if cur in storage:
    #             return True
    #         storage.add(cur)
    #         cur = cur.next
    #     return False
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pp1 = head
        pp2 = head
        while pp1 and pp2:
            pp1 = pp1.next
            pp2 = pp2.next.next
            if pp1 == pp2:
                return True
        return False


def print_ll(head: Optional[ListNode]):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next


if __name__=='__main__':
    ll = ListNode(head[0])
    cur = ll
    cur_node = None
    if index == 0:
        cur_node = ll
    i = 1
    while i < len(head):
        cur.next = ListNode(head[i])
        cur = cur.next
        if i == index:
            cur_node = cur
        i += 1
    if index != -1:
        cur.next = cur_node
    sol = Solution()
    # print_ll(ll)
    print(sol.hasCycle(ll))
