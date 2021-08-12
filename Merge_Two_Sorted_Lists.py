class ListAlone:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge2lists(self, l1: ListAlone, l2: ListAlone) -> ListAlone:
        dummy = ListAlone()
        p = dummy
        while l1 and l2:
            if l1.val <= l2.val:
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


if __name__ == '__main__':
    s = Solution()
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    if l1 != []:
        L1 = ListAlone(l1[0])
        current1 = L1
        for i in range(1, len(l1)):
            tmp_l = ListAlone(l1[i])
            current1.next = tmp_l
            current1 = current1.next
    if l2 != []:
        L2 = ListAlone(l2[0])
        current2 = L2
        for i in range(1, len(l2)):
            tmp_l = ListAlone(l2[i])
            current2.next = tmp_l
            current2 = current2.next
    L1 = None if l1 == [] else L1
    L2 = None if l2 == [] else L2
    if L2 == None and L1 == None:
        node = []
    if L2 != None and L1 != None:
        node = s.merge2lists(L1, L2)
    if L2 != None:
        node = L2
    if L1 != None:
        node = L1
    while node:
        print(node.val)
        node = node.next
