from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num = 0
        for i in nums:
            num ^= i
        i = (~num+1)&num
        a = b = 0
        for num in nums:
            if num&i:
                a ^= num
            else:
                b ^= num
        return [a, b]