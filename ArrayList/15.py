from typing import List

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