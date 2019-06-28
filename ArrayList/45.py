from collections import deque
from typing import List

class Solution_BFS:
    # BFS break time limitation
    def jump(self, nums: List[int]) -> int:
        length = len(nums)-1
        queue = deque([0])
        res = 0
        while queue:
            for _ in range(len(queue)):
                idx = queue.popleft()
                if idx==length:
                    return res
                elif idx>length:
                    continue
                else:
                    for i in range(nums[idx], 0, -1):
                        queue.append(idx+i)
            res += 1

class Solution:
    # From the end back to start
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        if length<=1:
            return 0
        else:
            max_val = max(nums)
            i, res = length-1,0
            ranges = range(1,max_val+1)
            while True:
                cur = i
                for idx, val in enumerate(ranges,1):
                    new_idx = cur-val
                    if new_idx>=0:
                        if nums[new_idx]>=idx:
                            if new_idx==0:
                                return res+1
                            else:
                                i = new_idx
                res += 1

# We can use greedy algorithm too.