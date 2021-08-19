from typing import List

class ListAlone:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def Merge2Lists(self, l1: ListAlone, l2: ListAlone)-> ListAlone:
        head = ListAlone()
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return head.next

    def GenSortedList(self, lists: List[ListAlone])->ListAlone:
        L = ListAlone()
        dummy = L
        for i in range(len(lists)):
            current = self.Merge2Lists(dummy.next, lists[i])
            dummy.next = current
            dummy = dummy.next
        return L.next


if __name__ == '__main__':
    s = Solution()
    lists = [[1,4,5],[1,3,4],[2,6],[8,9]]
    linked_list = []
    for l in lists:
        head = ListAlone(l[0])
        tmp = head
        for item in l[1:]:
            dummy = ListAlone(item)
            tmp.next = dummy
            tmp = tmp.next
        linked_list.append(head)
    node = s.GenSortedList(linked_list)
    index = 0
    while node:
        print(node.val)
        node = node.next
    #     index += 1
    # print(index)


    # node = s.GenSortedList(l)

