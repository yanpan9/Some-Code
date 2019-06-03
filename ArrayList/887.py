class Solution_DP1:
    # https://github.com/Shellbye/Shellbye.github.io/issues/42
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
        for i in range(1, N+1):
            dp[1][i]=i
        for i in range(2, K+1):
            x = 1
            for j in range(1, N+1):
                while x < j:
                    # max(T_1(x), T_2(x)) < max(T_1(x+1), T_2(x+1))
                    # which present x is the max time point in range
                    if max(dp[i-1][x-1], dp[i][j-x]) < max(dp[i-1][x], dp[i][j-x-1]):
                        break
                    else:
                        x += 1
                dp[i][j] = 1 + max(dp[i-1][x-1], dp[i][j-x])
        return dp[-1][-1]

class Solution_DP2:
    # https://github.com/Shellbye/Shellbye.github.io/issues/42
    # dp[k][m]: How many floors k eggs and m moves can check?
    # dp[k][m] = dp[k-1][m-1]+dp[k][m-1]+1
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [0 for _ in range(K+1)]
        m = 0
        while dp[-1] < N:
            for k in range(K, 0, -1):
                dp[k] = dp[k]+dp[k-1]+1
            m += 1
        return m