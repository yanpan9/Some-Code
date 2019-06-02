# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 1, n
        while L<R:
            mid = int((L+R)/2)
            if isBadVersion(mid):
                R = mid-1
            else:
                L = mid+1
        if isBadVersion(L):
            return L
        else: 
            return L+1