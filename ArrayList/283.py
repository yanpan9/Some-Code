from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        slow = idx = 0
        while idx < length:
            if nums[idx]:
                nums[idx], nums[slow] = nums[slow], nums[idx]
                slow += 1
            idx += 1