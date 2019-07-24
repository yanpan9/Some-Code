from typing import List

class cmp(str):
    def __lt__(x, y):
        return x+y < y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=cmp, reverse=True)
        res = "".join(nums)
        return "0" if res[0]=="0" else res