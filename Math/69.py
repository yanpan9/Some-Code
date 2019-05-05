class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r>x:
            print(r)
            r = int((r+x/r)/2)
        return r