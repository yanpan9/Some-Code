from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort(), s.sort()
        idx_g, idx_s = 0, 0
        len_g, len_s = len(g), len(s)
        while idx_g<len_g and idx_s<len_s:
            if g[idx_g]<=s[idx_s]:
                idx_g+=1
                idx_s+=1
                count += 1
            else:
                idx_s+=1
        return count