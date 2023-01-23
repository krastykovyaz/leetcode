from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is [] or lists == []:
            return []
        head = ListNode()
        head_cp = head
        i = 0
        while i < len(lists):
            tmp = self.merge2Lists(head_cp.next, lists[i])
            head_cp.next = tmp
            i += 1
        return head_cp.next

    def merge2Lists(self, left: Optional[ListNode], right: Optional[ListNode]):
        head = ListNode()
        head_cp = head
        while left and right:
            if left.val < right.val:
                head_cp.next = left
                left = left.next
            else:
                head_cp.next = right
                right = right.next
            head_cp = head_cp.next
        if left:
            head_cp.next = left
        if right:
            head_cp.next = right
        return head.next

    def printl(self, root):

        while root:
            print(root.val)
            root = root.next

def connection(nums):
    # if any(nums) == False:
    #     return []
    head = ListNode(nums[0])
    head_cp = head
    i = 1
    while i < len(nums):
        head_cp.next = ListNode(nums[i])
        head_cp = head_cp.next
        i += 1
    return head

if __name__=='__main__':
    s = Solution()
    nums = [[1], [0]]
    new_nums = list()
    for num in nums:
        num = connection(num)
        new_nums.append(num)
    for num in new_nums:
        while num:
            num = num.next
    root = s.mergeKLists(new_nums)
    s.printl(root)
    # while root:
    #     print(root.val)
    #     root = root.next

