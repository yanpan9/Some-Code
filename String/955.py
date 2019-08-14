from typing import List

class Solution_BruteForce:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        m = len(A)
        if m:
            n = len(A[0])
            if n:
                idx = 0
                while idx<n:
                    for i in range(1,m):
                        if A[i]<A[i-1]:
                            if A[i][idx]<A[i-1][idx]:
                                A = [s[:idx]+s[idx+1:] for s in A]
                                n -= 1
                                res += 1
                                break
                            else:
                                continue
                    else:
                        idx += 1
        return res

class Solution_Cuts:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        cuts = [False]*(m-1)
        res = 0
        for col in zip(*A):
            if all(cuts[i] or col[i]<=col[i+1] for i in range(m-1)):
                for i in range(m-1):
                    if col[i]<col[i+1]:
                        cuts[i] = True
            else:
                res += 1
        return res
        