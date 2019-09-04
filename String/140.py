from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = list()
        if not (s and wordDict):
            return self.res
        self.l = len(s)
        self.lw = max(len(w) for w in wordDict)
        self.words = set(wordDict)
        dp = [False for _ in range(self.l+1)]
        dp[0] = True
        for i in range(0, self.l+1):
            if dp[i]:
                for j in range(1, self.lw+1):
                    if i+j<=self.l and s[i:i+j] in self.words:
                        dp[i+j] = True
        if dp[-1]:
            self.dfs(s, dp, 0, list())
        return self.res
        
    def dfs(self, s, dp, idx, lst):
        if idx==self.l:
            self.res.append(" ".join(lst))
        else:
            for j in range(1, 1+self.lw):
                if idx+j<=self.l and dp[idx+j] and s[idx:idx+j] in self.words:
                    lst.append(s[idx:idx+j])
                    self.dfs(s, dp, idx+j, lst)
                    lst.pop()