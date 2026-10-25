# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

# Example 1:

# Input: 
temperatures = [30,38,30,36,35,40,28]

# Output: [1,4,1,2,1,0,0]
# Example 2:

# Input: 
# temperatures = [22,21,20]

# Output: [0,0,0]
from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    n = len(temperatures)
    res = [0] * n
    for i in range(len(temperatures) - 1, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res
            


if __name__=='__main__':
    # temperatures = [2, 1, 1, 3]
    print(dailyTemperatures(temperatures))
