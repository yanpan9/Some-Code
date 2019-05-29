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