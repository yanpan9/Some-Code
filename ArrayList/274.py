from typing import List
from collections import Counter

class Solution_BF:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        counter = Counter(citations)
        keys = sorted(counter.keys())
        l = len(keys)
        cumsum = [0 for _ in keys]
        val = 0
        for i in range(l):
            val += counter[keys[i]]
            cumsum[i] = val
        num = cumsum[-1]
        res = 0
        for i in range(l):
            key = keys[i]
            if i == 0:
                val = num
            else:
                val = num - cumsum[i-1]
            sub = min(key, val)
            if res < sub:
                res = sub
        return res

class Solution_Bucket:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        if l:
            bucket = [0]*(l+1)
            for i in citations:
                if i >= l:
                    bucket[l] += 1
                else:
                    bucket[i] += 1
            cur = 0
            for i in range(l, -1, -1):
                cur += bucket[i]
                if cur>=i:
                    return i
        else:
            return 0