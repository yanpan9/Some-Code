from typing import List

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        m = len(A)
        if m:
            n = len(A[0])
            if n:
                for i in range(n):
                    for j in range(1, m):
                        if A[j][i]<A[j-1][i]:
                            res += 1
                            break
        return res