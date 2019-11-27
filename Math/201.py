from typing import List

class Solution_1:
	# My method
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        lst = self.num2lst(m)
        res = self.residuals(lst)
        bit = 2
        idx, bit = 0, 1
        l = len(lst)
        while idx<l:
            if lst[idx]:
                if m+res[idx]<=n:
                    lst[idx] = 0
                else:
                    break
            idx += 1
            bit = bit<<1
        return self.lst2num(lst)
                
    
    def num2lst(self, m: int) -> List[int]:
        if not m:
            return [0]
        else:
            res = list()
            while m:
                q, r = divmod(m, 2)
                res.append(r)
                m = q
        return res
    
    def residuals(self, lst: List[int]) -> List[int]:
        s, b = 2, 1
        res = list()
        sum_ = 0
        for num in lst:
            sum_ += num*b
            res.append(s-sum_)
            s, b = s<<1, s
        return res
    
    def lst2num(self, lst: List[int]) -> int:
        res, bit = 0, 1
        for num in lst:
            res += num*bit
            bit = bit<<1
        return res

class Solution_2:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        cnt = 0
        while m!=n:
            m >>= 1
            n >>= 1
            cnt += 1
        return n<<cnt