class Solution:
    def climbStairs(self, n: int) -> int:
        fst, snd = 1, 1
        if n == 1:
            return snd
        else:
            count = 1
            while count < n:
                fst, snd = snd, fst+snd
                count += 1
            return snd