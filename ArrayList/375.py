class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n-1, 0, -1):
            for j in range(i+1, n+1):
                res = list()
                for k in range(i,j):
                    res.append(max(k+dp[i][k-1], k+dp[k+1][j]))
                dp[i][j]=min(res)
        return dp[1][-1]