from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m:
            n = len(matrix[0])
            if n:
                x_set, y_set = set(), set()
                for i in range(m):
                    for j in range(n):
                        if matrix[i][j]==0:
                            x_set.add(i)
                            y_set.add(j)
                for i in range(m):
                    for j in range(n):
                        if i in x_set or j in y_set:
                            matrix[i][j] = 0