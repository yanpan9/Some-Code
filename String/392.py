class Solution_DP:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        dp = [[0 for _ in range(len_t+1)] for _ in range(len_s+1)]
        for i_t, c_t in enumerate(t,1):
            for i_s, c_s in enumerate(s,1):
                if c_t==c_s:
                    dp[i_s][i_t]=dp[i_s-1][i_t-1]+1
                else:
                    dp[i_s][i_t]=max(dp[i_s-1][i_t], dp[i_s][i_t-1])
        return dp[-1][-1]==len(s)