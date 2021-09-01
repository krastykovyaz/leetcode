from typing import List
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def Reverse(self, head: Node)->Node:
        if head == None or head.next == None:
            return None
        dummy = head
        prev = None
        while dummy:
            nxt = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = nxt
        head = prev
        return head


if __name__=='__main__':
    s = Solution()
    d = [1, 2, 3, 4, 5]
    lst1 = Node(d[0])
    lst = lst1
    for i in range(1, len(d)):
        tmp = Node(d[i])
        lst.next = tmp
        lst = lst.next
    n = len(d)
    head = s.Reverse(lst1)
    while n:
        print(head.val)
        head = head.next
        n -= 1
