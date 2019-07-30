from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(idx):
            if idx == 9*9:
                return True
            else:
                i, j = divmod(idx, 9)
                if board[i][j]==blank:
                    for num in rg:
                        num += 1
                        if (num not in rows[i] and
                            num not in cols[j] and
                            num not in boxs[i//3][j//3]):
                            board[i][j]=str(num)
                            rows[i].add(num)
                            cols[j].add(num)
                            boxs[i//3][j//3].add(num)
                            if dfs(idx+1):
                                return True
                            board[i][j] = blank
                            rows[i].remove(num)
                            cols[j].remove(num)
                            boxs[i//3][j//3].remove(num)
                else:
                    if dfs(idx+1):
                        return True
                
        rg,blank = range(9), "."
        rows = [set() for _ in rg]
        cols = [set() for _ in rg]
        boxs = [[set() for _ in range(3)] for _ in range(3)]
        for i in rg:
            for j in rg:
                if board[i][j]!=blank:
                    ele = int(board[i][j])
                    rows[i].add(ele)
                    cols[j].add(ele)
                    boxs[i//3][j//3].add(ele)
        dfs(0)