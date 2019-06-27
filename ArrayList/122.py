from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        sum_ = 0
        for i in range(0, length-1):
            sub_ = prices[i+1]-prices[i]
            if sub_>0:
                sum_ += sub_
        return sum_