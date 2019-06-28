from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        max_val = 1
        for idx,num in enumerate(nums,1):
            if num==0:
                if max_val > idx:
                    continue
                else:
                    break
            else:
                max_val = max(max_val, idx+num)
        return max_val>=length