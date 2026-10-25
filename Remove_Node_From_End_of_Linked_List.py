# You are given the beginning of a linked list head, and an integer n.

# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:

# Input: 
# head = [1,2,3,4]
# n = 2

# Output: [1,2,4]
# Example 2:

# Input: 
head = [5]
n = 1

# Output: []
# Example 3:

# Input: head = [1,2], n = 2

# Output: [2]

class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

class Solution:
    def RemoveNode(self, head_, n):
        dummy = ListNode(0, head_)
        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next
        # print_ll(slow)
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        print_ll(head_)
    
def print_ll(root):
    cur = root
    while cur:
        print(cur.val)
        cur = cur.next

if __name__=='__main__':
    s = Solution()
    r = ListNode(head[0])
    cur = r
    i = 1
    while i < len(head):
        cur.next = ListNode(head[i])
        cur = cur.next
        i += 1
    # print_ll(r)
    s.RemoveNode(r, n)
