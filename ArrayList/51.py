from typing import List

class Solution_Array:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.array = list()
        self.size = n
        self.res = list()
        self.backTracking(0)
        return self.res
        
    def ifValid(self, row, col):
        for r,c in enumerate(self.array):
            if abs(col-c) in (0, row-r):
                return False
        else:
            return True
        
    def printBoard(self):
        board = [["." for _ in range(self.size)] for _ in range(self.size)]
        for row,col in enumerate(self.array):
            board[row][col]="Q"
        return ["".join(row) for row in board]
    
    def backTracking(self, row: int):
        if row<self.size:
            for i in range(self.size):
                if self.ifValid(row, i):
                    self.array.append(i)
                    self.backTracking(row+1)
                    self.array.pop()
        else:
            self.res.append(self.printBoard())

class Solution_Bits:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.upperlim = (1<<n)-1
        self.array = list()
        self.size = n
        self.res = list()
        self.backTracking(0, 0, 0)
        return self.res
    
    def binary2Col(self, p):
        i = -1
        while p:
            i += 1
            p = p>>1
        return i
    
    def printBoard(self):
        board = [["." for _ in range(self.size)] for _ in range(self.size)]
        for row,col in enumerate(self.array):
            board[row][col]="Q"
        return ["".join(row) for row in board]
    
    def backTracking(self, row: int, ld: int, rd: int):
        if row != self.upperlim:
            # cal the valid 1 in this row
            pos = self.upperlim&(~(row|ld|rd))
            while pos:
                # take a 1 from pos
                p = pos&(~pos+1)
                # remove p from pos
                pos = pos - p
                self.array.append(self.binary2Col(p))
                self.backTracking(row|p, (ld|p)<<1, (rd|p)>>1)
                self.array.pop()
        else:
            self.res.append(self.printBoard())