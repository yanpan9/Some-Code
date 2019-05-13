class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = list()
        def dfs(lst, sum_, nums):
            if sum_ == target:
                res.append(lst[:])
            else:
                for idx,num in enumerate(nums):
                    if sum_ + num <= target:
                        lst.append(num)
                        dfs(lst, sum_ + num, nums[idx:])
                        lst.pop()
        dfs([], 0, candidates)
        return res
                    