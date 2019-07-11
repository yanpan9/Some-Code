from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k%length
        idx = count = 0
        while count<length:
            key = nums[idx]
            new_idx = (idx+k)%length
            while new_idx!=idx:
                key,nums[new_idx] = nums[new_idx],key
                new_idx = (new_idx+k)%length
                count += 1
            else:
                nums[new_idx] = key
                count += 1
            idx += 1