from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        head_cp = head
        while head_cp:
            head_cp_next = head_cp.next
            head_cp.next = prev
            prev = head_cp
            head_cp = head_cp_next
        return prev


if __name__=='__main__':
    nums = [1, 4, 6, 8, 10]
    head = ListNode(nums[0])
    head_cp = head
    i = 1
    while i < len(nums):
        head_cp.next = ListNode(nums[i])
        head_cp = head_cp.next
        i += 1
    s = Solution()
    root = s.reverseList(head)
    while root:
        print(root.val)
        root = root.next


