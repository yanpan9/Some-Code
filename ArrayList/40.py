class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = list()
        candidates.sort()
        def dfs(lst, sum_, nums):
            if sum_ == target:
                res.append(lst[:])
            else:
                visited = set()
                for idx,num in enumerate(nums):
                    if num in visited:
                        continue
                    else:
                        visited.add(num)
                        if sum_ + num <= target:
                            lst.append(num)
                            dfs(lst, sum_ + num, nums[idx+1:])
                            lst.pop()
        dfs([], 0, candidates)
        return res