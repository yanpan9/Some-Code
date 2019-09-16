from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        if l:
            low, high = 0, l
            while low < high:
                mid = (low+high)//2
                if citations[mid]>=(l-mid):
                    high = mid
                else:
                    low = mid + 1
            return l-high
        else:
            return 0