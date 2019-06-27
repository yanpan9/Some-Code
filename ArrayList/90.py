from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, length = list(), len(nums)
        def subsets_dfs(lst, nums, pos):
            num = None
            res.append(lst[:])
            for i in range(pos, length):
                if nums[i]!=num:
                    lst.append(nums[i])
                    subsets_dfs(lst, nums, i+1)
                    num = lst.pop()
        subsets_dfs([], nums, 0)
        return res