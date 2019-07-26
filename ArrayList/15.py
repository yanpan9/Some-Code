from typing import List
from operator import add,sub

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, visited = list(), set()
        def twosum(nums, sum_):
            hash_t = set()
            res = list()
            for num in nums:
                if sum_ - num in hash_t:
                    sub_res = [sum_-num, num]
                    if sub_res in res:
                        continue
                    else:
                        res.append(sub_res)
                else:
                    hash_t.add(num)
            return res
        for idx, num in enumerate(nums):
            if num in visited:
                continue
            else:
                visited.add(num)
                for sub_res in twosum(nums[idx+1:], -num):
                    res.append([num]+sub_res)
        return res

class Solution_DoublePoint:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        idx,length = 0,len(nums)
        res = list()
        while idx<length-2 and nums[idx]<=0:
            val = nums[idx]
            low, high = idx+1, length-1
            while low<high:
                sum_ = val+nums[low]+nums[high]
                if sum_==0:
                    res.append([val, nums[low], nums[high]])
                    high = self.nextEle(nums, high, sub, length)
                elif sum_<0:
                    low = self.nextEle(nums, low, add, length)
                else:
                    high = self.nextEle(nums, high, sub, length)
            idx = self.nextEle(nums, idx, add, length)
        return res

    def nextEle(self, nums, idx, oper, length):
        val = nums[idx]
        i = oper(idx,1)
        while i>=0 and i<length and nums[i]==val:
            i = oper(i, 1)
        return i