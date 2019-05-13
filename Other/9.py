class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0:
            digits = list()
            y = x
            while y:
                y, d = divmod(y, 10)
                digits.append(d)
            reverse_digits = digits[::-1]
            return reverse_digits==digits
        else:
            return False