from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        l = len(nums)
        self.dp = [0]*(l+1)
        for i in range(l):
            self.dp[i+1] = self.dp[i]+nums[i]
        print(self.dp)

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1]-self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)