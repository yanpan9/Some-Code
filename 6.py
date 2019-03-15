# ZigZag Conversion 1

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ""
        if numRows==1:
            return s
        step = 2*(numRows-1)
        res = list()
        length = len(s)
        for i in range(numRows):
            sp_1, sp_2 = step-2*i, 2*i
            if sp_1==step or sp_1==0:
                while i < length:
                    res.append(s[i])
                    i += step
            else:
                while i<length:
                    res.append(s[i])
                    i += sp_1
                    if i >=length:
                        break
                    res.append(s[i])
                    i += sp_2
        return "".join(res)

# ZigZag Conversion 2

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows==1:
            return s
        rows = [list() for _ in range(numRows)]
        row_idx = 0
        dire = 1
        for idx,char in enumerate(s):
            rows[row_idx].append(char)
            row_idx+=dire
            if row_idx==numRows-1:
                dire = -1
            if row_idx==0:
                dire = 1
        rows = ["".join(row) for row in rows]
        return "".join(rows)