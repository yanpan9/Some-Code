class Solution:
    def reverseBits(self, n: int) -> int:
        stack = list()
        while n:
            n, r = divmod(n,2)
            stack.append(r)  
        res = 0
        bit = 1<<(32-len(stack))
        while stack:
            res += bit*stack.pop()
            bit = bit<<1
        return res