from typing import List
from operator import add,sub

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		# 疯狂超时，我枯了
        nums.sort()
        start,length = 0,len(nums)
        res = list()
        while start<length-3:
            end = length - 1
            while end-start>=3:
                max_sum = nums[start]
                for i in range(3):
                    max_sum += nums[end-i]
                if max_sum < target:
                    break
                val = nums[start]+nums[end]
                low, high = start+1, end-1
                while low<high:
                    sum_ = val+nums[low]+nums[high]
                    if sum_==target:
                        res.append([nums[start], nums[low], nums[high], nums[end]])
                        low = self.nextEle(nums, low, add, length)
                        high = self.nextEle(nums, high, sub, length)
                    elif sum_<target:
                        low = self.nextEle(nums, low, add, length)
                    else:
                        high = self.nextEle(nums, high, sub, length)
                end = self.nextEle(nums, end, sub, length)
            start = self.nextEle(nums, start, add, length)
        return res

    def nextEle(self, nums, idx, oper, length):
        val = nums[idx]
        i = oper(idx,1)
        while i>=0 and i<length and nums[i]==val:
            i = oper(i, 1)
        return i