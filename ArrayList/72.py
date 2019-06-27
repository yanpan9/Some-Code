from typing import List

class Solution_Recursion:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsets_recur(nums):
            if len(nums)==1:
                yield nums
                yield []
            else:
                for res in subsets_recur(nums[1:]):
                    yield nums[:1]+res
                for res in subsets_recur(nums[1:]):
                    yield []+res
        return list(subsets_recur(nums))

class Solution_Backtracking:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, length = list(), len(nums)
        def subsets_dfs(lst, nums, pos):
            res.append(lst[:])
            for i in range(pos, length):
                lst.append(nums[i])
                subsets_dfs(lst, nums, i+1)
                lst.pop()
        subsets_dfs([], nums, 0)
        return res