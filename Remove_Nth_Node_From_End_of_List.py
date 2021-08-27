# Definition for singly-linked list.
class ListAlone:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def RemoveNode(self, head: ListAlone, n: int) -> ListAlone:
        if head == None:
            return []
        dummy = head
        index = 0
        while dummy:
            dummy = dummy.next
            index += 1
        prev = None
        tail = head
        while tail != None:
            if n == index:
                if prev:
                    prev.next = tail.next
                    return head
                else:
                    return tail.next
            prev = tail
            tail = tail.next
            index -= 1
        return head




if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4, 5]
    n = 2
    L = ListAlone(head[0])
    tmp = L
    for item in head[1:]:
        dummy = ListAlone(item)
        tmp.next = dummy
        tmp = tmp.next
    node = s.RemoveNode(L, n)
    while node:
        print(node.val)
        node = node.next
