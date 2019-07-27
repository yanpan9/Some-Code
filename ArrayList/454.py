from typing import List

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res, counter = 0, dict()
        for a in A:
            for b in B:
                key = a+b
                counter[key]=counter.get(key, 0)+1
        for c in C:
            for d in D:
                key=-c-d
                res += counter.get(key,0)
        return res