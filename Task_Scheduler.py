# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.
# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
# Return the minimum number of CPU cycles required to complete all tasks.

# Example 1:

# Input: 
tasks = ["X","X","Y","Y"]
n = 2

# Output: 5
# Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

# Example 2:

# Input: 
tasks = ["A","A","A","B","C"]
n = 3

# Output: 9
# Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.
from collections import defaultdict, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        alphabet = [0] * 26
        for task in tasks:
            alphabet[ord(task) - ord('A')] += 1
        alphabet = [-a for a in alphabet]
        heapq.heapify(alphabet)
        i = 0
        max_val = 0
        while i < len(alphabet):
            if alphabet[0] == alphabet[i]:
                max_val += 1
            i += 1

        return max(len(tasks), (-alphabet[0] - 1) * (n + 1) + max_val)



        
        




if __name__ == '__main__':
    s = Solution()
    print(s.leastInterval(tasks, n))

        