from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        if self.m:
            self.n = len(board[0])
            if self.n:
                self.dirs = ((0,1), (1,0), (-1, 0), (0, -1))
                self.word = word
                self.l = len(word)
                for i in range(self.m):
                    for j in range(self.n):
                        if board[i][j]==word[0]:
                            if self.dfs(board, [(i,j)], 1):
                                return True
                else:
                    return False
            else:
                return False
        return False
    
    def dfs(self, board, lst, w_idx):
        if w_idx==self.l:
            return True
        else:
            x, y = lst[-1]
            for dx, dy in self.dirs:
                nx, ny = x+dx, y+dy
                if nx>=0 and nx<self.m and ny>=0 and ny<self.n:
                    if (nx,ny) not in lst and board[nx][ny]==self.word[w_idx]:
                        lst.append((nx,ny))
                        if self.dfs(board, lst, w_idx+1):
                            return True
                        else:
                            lst.pop()