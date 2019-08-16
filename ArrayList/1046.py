from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        l = len(stones)
        while l>1:
            x = stones.pop()
            y = stones.pop()
            if x!=y:
                n = abs(x-y)
                stones.append(n)
                l -= 1
                idx = l-1
                while idx>=1 and stones[idx]<stones[idx-1]:
                    stones[idx],stones[idx-1] = stones[idx-1], stones[idx]
                    idx -= 1
            else:
                l -= 2
        return stones[0] if l else 0