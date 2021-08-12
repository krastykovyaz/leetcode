import timeit

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = int(''.join([str(item) for item in l1[-1::-1]]))
        l2 = int(''.join([str(item) for item in l2[-1::-1]]))
        l3 = l1 + l2
        l3 = [int(item) for item in list(str(l3))[-1::-1]]
        return l3

if __name__=='__main__':
    s = Solution()
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    print(s.addTwoNumbers(l1, l2))
    print(timeit.timeit(lambda: s.addTwoNumbers(l1, l2), number=1))
    