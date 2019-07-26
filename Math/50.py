class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n
        return self.fastPow(x, n)
        
    def fastPow(self, x, n):
        if x==1:
            return 1
        elif n==0:
            return 1
        else:
            val = self.myPow(x, n//2)**2
            if n%2:
                return val*x
            else:
                return val
                