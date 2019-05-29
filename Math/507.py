from math import sqrt

class Solution_Fast:
    def checkPerfectNumber(self, num: int) -> bool:
        # Euclid Perfect Number
        # If 2^p-1 is a prime
        # (Mersenne primes),
        # then (2^p-1)(2^(p-1)) is a 
        # perfect number
        per_num = {6, 28, 496, 8128, 33550336}
        return num in per_num

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if not num:
            return False
        res = 1
        while num%2==0:
            num = num/2
            res *= 2
        if res*2 == num+1 and res > 1:
            for i in range(2, int(sqrt(num))):
                if num%i == 0:
                    return False
            else:
                return True
        else:
            return False