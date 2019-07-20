from typing import List

class Solution_Backtracking:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = list()
        nums = list(range(1,n+1))
        self.dfs(list(), nums, k)
        return self.res
        
    def dfs(self, lst, nums, length):
        if length==0:
            self.res.append(lst[:])
        else:
            for idx,num in enumerate(nums):
                lst.append(num)
                new_nums = nums[idx+1:]
                if len(new_nums)>=length-1:
                    self.dfs(lst, new_nums, length-1)
                lst.pop()

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,k+1))+[n+1]
        res = list()
        j = 0
        while j<k:
            res.append(nums[:k])
            j = 0
            while j<k and nums[j]+1==nums[j+1]:
                nums[j] = j+1
                j += 1
            nums[j] += 1
        return res