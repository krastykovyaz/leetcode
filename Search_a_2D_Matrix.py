# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Input: 
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
# matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target=13

# Output: true
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1
    while left <= right:
        mid =(right + left) // 2
        val = matrix[mid // n][mid % n]
        if target == val:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
        # print(left, right)
    return False


        

if __name__=='__main__':
    print(searchMatrix(matrix, target))