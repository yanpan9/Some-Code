from typing import List
from operator import add,sub

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 2**31-1
        idx,length = 0,len(nums)
        while idx<length-2:
            val = nums[idx]
            low, high = idx+1, length-1
            while low<high:
                sum_ = val+nums[low]+nums[high]
                if sum_ == target:
                    return target
                elif sum_<target:
                    if target-sum_<abs(target-res):
                        res = sum_
                    low = self.nextEle(nums, low, add, length)
                else:
                    if sum_-target<abs(target-res):
                        res = sum_
                    high = self.nextEle(nums, high, sub, length)
            idx = self.nextEle(nums, idx, add, length)
        return res
    
    def nextEle(self, nums, idx, oper, length):
        val = nums[idx]
        i = oper(idx,1)
        while i>=0 and i<length and nums[i]==val:
            i = oper(i, 1)
        return i