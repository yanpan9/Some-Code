class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res, length = [1], 1
        p_2 = p_3 = p_5 = 0
        while length<n:
            num = min(res[p_2]*2, res[p_3]*3, res[p_5]*5)
            res.append(num)
            length += 1
            if num==res[p_2]*2:
                p_2 += 1
            if num==res[p_3]*3:
                p_3 += 1  
            if num==res[p_5]*5:
                p_5 += 1
        return res[-1]