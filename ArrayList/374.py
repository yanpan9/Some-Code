# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 1, n
        while True:
            mid = int((L+R)/2)
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                R = mid-1
            else:
                L = mid+1