from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x,y = click
        if board[x][y]=="M":
            board[x][y]="X"
            return board
        elif board[x][y]=="E":
            self.xrange = set(range(len(board)))
            self.yrange = set((range(len(board[0]))))
            count = self.countBoard(board, click)
            if count==0:
                board[x][y]="B"
                for i in range(-1,2):
                    for j in range(-1,2):
                        if x+i in self.xrange and y+j in self.yrange:
                            self.updateBoard(board, (x+i, y+j))
            else: 
                board[x][y]=str(count)
        return board
            
    def countBoard(self, board: List[List[str]], click: List[int]) -> int:
        x,y = click
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if x+i in self.xrange and y+j in self.yrange:
                    if board[x+i][y+j]=="M":
                        count += 1
        return count