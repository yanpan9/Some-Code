class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        length = len(A) 
        dp = dict()
        for i in range(length-1):
            for j in range(i+1, length):
                diff = A[j]-A[i]
                dp[j, diff]=dp.get((i, diff), 1)+1
        return max(dp.values())