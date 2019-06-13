class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1,],[1,1]]
        if numRows<=2:
            return res[:numRows]
        else:
            last_row, number = res[-1], 3
            while number <= numRows:
                row = [1 for i in range(number)]
                for i in range(1, number-1):
                    row[i] = last_row[i-1] + last_row[i]
                number += 1
                res.append(row)
                last_row = row
            return res