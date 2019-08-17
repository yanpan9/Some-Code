from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ninf = -2**32
        a = b = c = ninf
        for num in nums:
            if num>c:
                if num>b:
                    if num>a:
                        a, b, c = num, a, b
                    elif num<a:
                        b, c = num, b
                elif num<b:
                    c = num
        return a if c==ninf else c