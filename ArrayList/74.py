from typing import List

class Solution_BinarySearch:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m:
            n = len(matrix[0])
            if n:
                res = self.biSear([i[0] for i in matrix], target, 0, m-1)
                if isinstance(res, bool):
                    return True
                else:
                    _, high = res
                res = self.biSear(matrix[high], target, 0, n-1)
                return isinstance(res, bool)
            
    def biSear(self, array, target, low, high):
        while low<=high:
            mid = (low+high)//2
            if array[mid]==target:
                return True
            elif array[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return (low, high)

class Solution_Linear:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m:
            n = len(matrix[0])
            if n:
                idx = m-1
                while idx>=0 and matrix[idx][0]>target:
                    idx -= 1
                if idx==-1:
                    return False
                else:
                    return target in matrix[idx]