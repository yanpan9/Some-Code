from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m:
            n = len(matrix[0])
            if n:
                res = 0
                dp = [0 for _ in range(n+1)]
                for i in range(m):
                    prev = 0
                    for j in range(n):
                        temp = dp[j+1]
                        if matrix[i][j]=="1":
                            dp[j+1] = min((prev, dp[j], dp[j+1]))+1
                            if dp[j+1]>res:
                                res = dp[j+1]
                        else:
                            dp[j+1] = 0
                        prev = temp
                return res**2
        return 0