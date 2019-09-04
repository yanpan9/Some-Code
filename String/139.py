from typing import List
from collections import deque

class Solution_BFS:
	# ETL
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not (s and wordDict):
            return False
        l = len(s)
        lw = max(len(w) for w in wordDict)
        words = set(wordDict)
        queue = deque()
        queue.append(0)
        while queue:
            st = queue.popleft()
            if st==l:
                return True
            for i in range(1,lw+1):
                if s[st:st+i] in words:
                    queue.append(st+i)
        else:
            return False

class Solution_DP:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not (s and wordDict):
            return False
        l = len(s)
        lw = max(len(w) for w in wordDict)
        words = set(wordDict)
        dp = [False for _ in range(l+1)]
        dp[0] = True
        for i in range(0, l+1):
            if dp[i]:
                for j in range(1, lw+1):
                    if i+j<=l and s[i:i+j] in words:
                        dp[i+j] = True
        return dp[-1]