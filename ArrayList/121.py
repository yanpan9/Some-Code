class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = 100000
        max_ = 0
        for price in prices:
            if price<min_:
                min_ = price
            else:
                max_ = max(price-min_, max_)
        return max_