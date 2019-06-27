from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.check9elems(row):
                return False
        for i in range(9):
            col = [row[i] for row in board]
            if not self.check9elems(col):
                return False 
        for i in range(0,9,3):
            for j in range(0,9,3):
                block = list()
                for k in range(i,i+3):
                    block.extend(board[k][j:j+3])
                if not self.check9elems(block):
                    return False 
        return True
        
    def check9elems(self, elems: List[int]) -> bool:
        elems = [i for i in elems if i!="."]
        return len(set(elems))==len(elems)

class Solution_Hash:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rg, blank = range(9), "."
        rows = [set() for i in rg]
        cols = [set() for i in rg]
        boxs = [[set() for i in range(3)] for j in range(3)]
        for i in rg:
            for j in rg:
                if board[i][j] != blank:
                    ele = int(board[i][j])
                    if ele in rows[i]:
                        return False
                    else:
                        rows[i].add(ele)
                    if ele in cols[j]:
                        return False
                    else:
                        cols[j].add(ele)
                    if ele in boxs[i//3][j//3]:
                        return False
                    else:
                        boxs[i//3][j//3].add(ele)
        return True