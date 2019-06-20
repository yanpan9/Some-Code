class Solution:
    def totalNQueens(self, n: int) -> int:
        self.upperlim = (1<<n)-1
        self.size = n
        self.res = 0
        self.backTracking(0, 0, 0)
        return self.res
    
    def backTracking(self, row: int, ld: int, rd: int):
        if row != self.upperlim:
            # cal the valid 1 in this row
            pos = self.upperlim&(~(row|ld|rd))
            while pos:
                # take a 1 from pos
                p = pos&(~pos+1)
                # remove p from pos
                pos = pos - p
                self.backTracking(row|p, (ld|p)<<1, (rd|p)>>1)
        else:
            self.res += 1