from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m:
            n = len(matrix[0])
            if n:
                row, col = m-1, 0
                while row>=0 and col<n:
                    if matrix[row][col]==target:
                        return True
                    elif matrix[row][col]<target:
                        col += 1
                    else:
                        row -= 1
                else:
                    return False
            else:
                return False
        else:
            return False