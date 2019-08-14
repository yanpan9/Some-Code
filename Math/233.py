class Solution:
    def __init__(self):
        self.map = {0:0, 9:1}
        for i in range(1, 10):
            self.map[10**(i+1)-1] = 10**i+10*(self.map[10**i-1])
    
    def countDigitOne(self, n: int) -> int:
        if n<=0:
            return 0
        i = 1
        while i*10<=n:
            i *= 10
        return int(self.count(n ,i))

    def count(self, n, i):
        if n==0:
            return 0
        else:
            while i>n:
                i /= 10
            n_1 = self.map[i-1]
            return min(i, n-i+1)+n//i*n_1+self.count(n%i, i/10)