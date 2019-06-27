from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return list(self._subsets([], nums))
    
    def _subsets(self, lst: List[int], nums: List[int]) -> List[int]:
            yield lst[:]
            for i,v in enumerate(nums):
                lst.append(v)
                for sub_res in self._subsets(lst, nums[i+1:]):
                    yield sub_res
                lst.pop()