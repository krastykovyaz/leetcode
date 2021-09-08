# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        while l1:
            list1.append(str(l1.val))
            l1 = l1.next
        list2 = []
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next
        list3 = str(int(''.join(list1)) + int(''.join(list2)))
        l3 = [int(w) for w in list3]
        l3 = l3[::-1]
        L3 = ListNode(l3[0])
        dummy3 = L3
        for l in l3[1:]:
            tmp = ListNode(l)
            dummy3.next = tmp
            dummy3 = dummy3.next
        return L3

# if __name__=='__main__':
#     s = Solution()
#     l1 = [2,4,3]
#     l2 = [5,6,4]
#     L1 = ListNode(l1[0])
#     dummy1 = L1
#     for i in l1[1:]:
#         tmp = ListNode(i)
#         dummy1.next = tmp
#         dummy1 = dummy1.next
#     L2 = ListNode(l2[0])
#     dummy2 = L2
#     for i in l2[1:]:
#         tmp = ListNode(i)
#         dummy2.next = tmp
#         dummy2 = dummy2.next
#     print(s.addTwoNumbres(L1, L2))