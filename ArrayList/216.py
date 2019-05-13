class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = list()
        nums = list(range(1,10 if n>10 else n))
        def dfs(lst, k, sum_, nums):
            if k == 0:
                if sum_ == n:
                    res.append(lst[:])
                else:
                    pass
            elif k > 0:
                for idx,num in enumerate(nums):
                    if sum_ + num <= n:
                        lst.append(num)
                        dfs(lst, k-1, sum_ + num, nums[idx+1:])
                        lst.pop()
        dfs([], k, 0, nums)
        return res