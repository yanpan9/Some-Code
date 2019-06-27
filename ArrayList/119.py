from typing import List

class Solution_Normal:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex<=1:
            return [1]*(rowIndex+1)
        else:
            last_row, number = [1,1], 2
            while number <= rowIndex:
                row = [1 for i in range(number+1)]
                for i in range(1, number):
                    row[i] = last_row[i-1] + last_row[i]
                number += 1
                last_row = row
            return last_row

class Solution_Math:
    # C(n, i) = (n-i)!i!/n!
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(0, rowIndex):
            res.append(res[-1]*(rowIndex-i)//(i+1))
        return res