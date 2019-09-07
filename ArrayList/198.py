from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums:
            l = len(nums)
            a, b = 0, 0
            i = 0
            while i<l:
                a, b = b, max(a+nums[i], b)
                i += 1
            return b
        else:
            return 0