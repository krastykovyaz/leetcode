from typing import List


class Solution:
    def ReverseMatrix(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
        return matrix


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.ReverseMatrix(matrix))
