# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
# The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.
# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Return the sum of the two numbers as a linked list.

# Input: 
l1 = [1,2,3]
l2 = [4,5,6]
# Output: [5,7,9]
# Explanation: 321 + 654 = 975.
# Example 2:
# Input: 
# l1 = [9]
# l2 = [9]
# Output: [8,1]
from typing import Optional

class ListNode:
    def __init__(self, val=0, next_ = None):
        self.val = val
        self.next = next_

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        rest = 0
        while l1 or l2:
            total = rest
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            rest = total // 10
            total %= 10
            cur.next = ListNode(total)
            cur = cur.next
        if rest:
            cur.next = ListNode(rest)
            cur = cur.next
        print_ll(dummy.next)
        return dummy.next


def print_ll(root):
    cur = root
    while cur:
        print(cur.val)
        cur = cur.next

if __name__ == '__main__':
    list1 = ListNode(l1[0])
    cur = list1
    i = 1
    while i < len(l1):
        cur.next = ListNode(l1[i])
        cur = cur.next
        i += 1
    list2 = ListNode(l2[0])
    cur = list2
    i = 1
    while i < len(l2):
        cur.next = ListNode(l2[i])
        cur = cur.next
        i += 1
    s = Solution()
    print(s.addTwoNumbers(list1,list2))
