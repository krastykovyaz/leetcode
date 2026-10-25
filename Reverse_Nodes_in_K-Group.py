# You are given the head of a singly linked list head and a positive integer k.

# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

# Return the modified list after reversing the nodes in each group of k.

# You are only allowed to modify the nodes' next pointers, not the values of the nodes.

# Example 1:

# Input: 
head = [1,2,3,4,5,6]
k = 3

# Output: [3,2,1,6,5,4]
# Example 2:

# Input: 
# head = [1,2,3,4,5]
# k = 3

# Output: [3,2,1,4,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kht = group_prev
            for _ in range(k):
                kht = kht.next
                if not kht:
                    return dummy.next
            group_next = kht
            prev = group_next.next
            cur = group_prev.next
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            tmp = group_prev.next
            group_prev.next = prev
            group_prev = tmp
        


def print_ll(node):
    root = node
    while root:
        print(root.val)
        root = root.next


if __name__=='__main__':
    s = Solution()
    # s.reverseKGroup()
    root = ListNode(head[0])
    cur = root
    i = 1
    while i < len(head):
        cur.next = ListNode(head[i])
        cur = cur.next
        i += 1
    # print_ll(s._reverse(root))
    # print_ll(s.reverseKGroup(root, k))
    print_ll(s.reverseKGroup(root, k))