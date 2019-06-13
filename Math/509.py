class Solution:
    def fib(self, N: int) -> int:
        fst, snd = 0, 1
        if N == 0:
            return fst
        elif N == 1:
            return snd
        else:
            count = 1
            while count < N:
                fst, snd = snd, fst+snd
                count += 1
            return snd