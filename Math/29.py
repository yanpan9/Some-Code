class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend<0) ^ (divisor<0):
            sign = 0
        else:
            sign = 1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        for i in range(31, -1, -1):
            while (dividend >> i) >= divisor:
                res += 1<<i
                dividend -= divisor<<i
        res = res if sign else -res
        if res>2**31-1 or res<-2**31:
            res = 2**31 -1
        return res