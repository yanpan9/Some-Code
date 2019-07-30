from typing import List

class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        if N:
            board = [[N for _ in range(N)] for _ in range(N)]
            for ele in mines:
                board[ele[0]][ele[1]] = 0
            for i in range(N):
                up = left = bot = right = 0
                for j in range(N):
                    up = up+1 if board[i][j] else 0
                    if up<board[i][j]:board[i][j]=up
                    left = left+1 if board[j][i] else 0
                    if left<board[j][i]:board[j][i]=left
                for j in range(N-1,-1,-1):
                    bot = bot+1 if board[i][j] else 0
                    if bot<board[i][j]:board[i][j]=bot
                    right = right+1 if board[j][i] else 0
                    if right<board[j][i]:board[j][i]=right
            return max([max(row) for row in board])
        return 0