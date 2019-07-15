class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        else:
            array = [True for _ in range(n)]
            array[0] = array[1] = False
            for i in range(2, n):
                if array[i]:
                    num, i = i, i+i
                    while i<n:
                        array[i] = False
                        i += num
            return sum(array)