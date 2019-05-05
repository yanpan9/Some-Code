class Solution_DP:
    def isMatch(self, s: str, p: str) -> bool:
        ques, star = "?", "*"
        len_s, len_p = len(s), len(p)
        dp = [[False for j in range(len_p+1)] for i in range(len_s+1)]
        dp[0][0]=True
        for j in range(1,len_p+1):
            if p[j-1]==star and dp[0][j-1]:
                dp[0][j]=True
        for i in range(1,len_s+1):
            for j in range(1,len_p+1):
                if s[i-1]==p[j-1] or p[j-1]==ques:
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]==star:
                    dp[i][j]=(dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1])
        return dp[-1][-1]