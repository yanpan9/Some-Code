from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permutation(nums):
            if len(nums)==1:
                yield nums
            else:
                choosed = set()
                for idx in range(len(nums)):
                    ele = nums[idx]
                    if ele not in choosed:
                        choosed.add(ele)
                        ele = [ele]
                        for res in permutation(nums[:idx]+nums[idx+1:]):
                            yield ele+res
        return list(permutation(nums))