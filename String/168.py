from collections import deque

class Solution:
    def convertToTitle(self, n: int) -> str:
        base = ord("A")
        num2alpha = {i+1:chr(i+base) for i in range(26)}
        res = deque()
        while n:
            n, rem = divmod(n,26)
            if rem==0:
                res.appendleft(num2alpha[26])
                n -= 1
            else:
                res.appendleft(num2alpha[rem])
        return "".join(res)