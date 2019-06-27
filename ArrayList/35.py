from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if target<=nums[0]:
            return 0
        elif target>nums[-1]:
            return length
        else:
            L, R = 0, length-1
            while True:
                mid = int((L+R)/2)
                if nums[mid]<target:
                    L = mid
                else:
                    R = mid
                if L+1 == R:
                    return R