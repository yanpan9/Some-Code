from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        front, back = 0, 1
        while back < length:
            if nums[back]==nums[front]:
                back += 1
            else:
                front += 1
                nums[front] = nums[back]
                back += 1
        if length == 0:
            return 0
        else:
            return front + 1