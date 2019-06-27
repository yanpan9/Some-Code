from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left, right = 0, length-1
        i = 0
        while i <= right:
            if nums[i]==0:
                if i==left:
                    pass
                else:
                    nums[i] = nums[left]
                    nums[left] = 0
                i += 1
                left += 1
            elif nums[i]==2:
                nums[i] = nums[right]
                nums[right] = 2
                right -= 1
            else:
                i += 1