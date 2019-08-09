from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==0:
            return list(list())
        else:
            matrix = [[0 for _ in range(n)] for _ in range(n)]
            idx = 1
            up = left = 0
            bot = right = n-1
            while idx <= n*n:
                for i,j in self.spiralIndex(up, bot, left, right):
                    matrix[i][j]=idx
                    idx += 1
                up = left = up+1
                bot = right = bot-1
            return matrix
                
                
    def spiralIndex(self, up, bot, left, right):
        for j in range(left, right+1):
            yield up, j
        for i in range(up+1, bot+1):
            yield i, right
        if up<bot and left<right:
            for j in range(right-1, left-1, -1):
                yield bot,j
            for i in range(bot-1, up, -1):
                yield i,left