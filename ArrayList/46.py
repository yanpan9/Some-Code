class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(nums):
            if len(nums)==1:
                yield nums
            else:
                for idx in range(len(nums)):
                    ele = nums[idx:idx+1]
                    for res in permutation(nums[:idx]+nums[idx+1:]):
                        yield ele+res
        return list(permutation(nums))

class Solution_Backtracking:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        def dfs(lst, nums):
            if not nums:
                result.append(lst[:])
            else:
                for i,v in enumerate(nums):
                    lst.append(v)
                    dfs(lst, nums[:i]+nums[i+1:])
                    lst.pop()
        dfs(list(), nums)
        return result