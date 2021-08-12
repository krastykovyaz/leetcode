from typing import List

class ListAlone:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def Merge2Lists(self, l1: ListAlone, l2: ListAlone)-> ListAlone:
        dummy = ListAlone()
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l2:
            p.next = l2
        if l1:
            p.next = l1
        return dummy.next




    def GenSortedList(self, lists: List[ListAlone])->ListAlone:
        n = len(lists)
        L = ListAlone()
        dummy = L
        for i in range(n):
            current = self.Merge2Lists(dummy.next, lists[i])
            dummy.next = current
            dummy = dummy.next
        return L.next


if __name__ == '__main__':
    s = Solution()
    lists = [[1,4,5],[1,3,4],[2,6],[8,9]]
    linked_list = []
    # dummy = ListAlone()
    # p = dummy
    for l in lists:
        start = ListAlone(l[0])
        node = start
        for val_in_l in l[1:]:
            current = ListAlone(val_in_l)
            node.next = current
            node = node.next
        # p.next = start
        # while p.next:
        #     p = p.next
        linked_list.append(start)
    node = s.GenSortedList(linked_list)
    index = 0
    while node:
        print(node.val)
        node = node.next
    #     index += 1
    # print(index)


    # node = s.GenSortedList(l)

