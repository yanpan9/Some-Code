class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        if l and s[0]!="0":
            dp = [0 for _ in range(l+1)]
            dp[0] = dp[1] = 1
            for i in range(1, l):
                dp[i+1] = 0 if s[i]=="0" else dp[i]
                num = int(s[i-1:i+1])
                if num>=10 and num<=26:
                    dp[i+1] += dp[i-1]
            return dp[-1]
        else:
            return 0