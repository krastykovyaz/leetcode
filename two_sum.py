# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def Sum2Arrays(arr1, arr2):
    add = 0
    sum_arr = []
    if len(arr1) < len(arr2): arr1, arr2 = arr2, arr1
    for i in range(len(arr1)):
        if i < len(arr2):
            sum_arr.append((arr2[i] + arr1[i] + add) % 10)
            add = (arr2[i] + arr1[i] + add) // 10
        else:
            sum_arr.append((arr1[i] + add) % 10)
            add = (arr1[i] + add) // 10
    if add > 0:
        sum_arr.append(1)
    return sum_arr


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        list2 = []
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        l3 = Sum2Arrays(list2, list1)
        L3 = ListNode(l3[0])
        dummy3 = L3
        for l in l3[1:]:
            tmp = ListNode(l)
            dummy3.next = tmp
            dummy3 = dummy3.next
        return L3


if __name__ == '__main__':
    s = Solution()
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    L1 = ListNode(l1[0])
    dummy1 = L1
    for i in l1[1:]:
        tmp = ListNode(i)
        dummy1.next = tmp
        dummy1 = dummy1.next
    L2 = ListNode(l2[0])
    dummy2 = L2
    for i in l2[1:]:
        tmp = ListNode(i)
        dummy2.next = tmp
        dummy2 = dummy2.next
    ListOut = s.addTwoNumbers(L1, L2)
    dummy = ListOut
    while dummy:
        print(dummy.val)
        dummy = dummy.next


