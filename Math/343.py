class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i//2+1):
                x = j if j>dp[j] else dp[j]
                y = i-j if (i-j)>dp[i-j] else dp[i-j]
                if x*y>dp[i]:
                    dp[i] = x*y
        return dp[n]