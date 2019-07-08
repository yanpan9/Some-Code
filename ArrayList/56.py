from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        idx, length = 0, len(intervals)
        res = list()
        while idx<length:
            start, end = intervals[idx]
            new_idx = idx
            while new_idx<length-1 and end>=intervals[new_idx+1][0]:
                new_idx+=1
                end = max(end, intervals[new_idx][1])
            res.append([start, end])
            idx = new_idx+1
        return res