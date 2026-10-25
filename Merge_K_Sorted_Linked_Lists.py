# You are given an array of k linked lists lists, where each list is sorted in ascending order.

# Return the sorted linked list that is the result of merging all of the individual linked lists.

# Example 1:

# Input: 
lists = [[1,2,4],[1,3,5],[3,6]]

# Output: [1,1,2,3,3,4,5,6]
# Example 2:

# Input: lists = []

# Output: []
# Example 3:

# Input: lists = [[]]

# Output: []

# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not any(lists):
            return
        head = None
        for i in range(0, len(lists)):
            head = self.mergeTwoLists(head, lists[i])
        return head

    def mergeTwoLists(self, list1, list2):
        l1 = list1
        l2 = list2
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next

        
        cur.next = l1 or l2

        return dummy.next
        




def print_ll(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next

def print_arr_ll(arr):
    for ar in arr:
        print_ll(ar)

if __name__=='__main__':
    s = Solution()
    def form_llinst(arr):
        root = ListNode(arr[0])
        cur = root
        i = 1
        while i < len(arr):
            cur.next = ListNode(arr[i])
            cur = cur.next
            i += 1
        return root

    llists = []
    for lst in lists:
        llists.append(form_llinst(lst))
    # s.mergeKLists(llists)
    # print_arr_ll(llists)
    print_ll(s.mergeKLists(llists))