class Solution:
    def titleToNumber(self, s: str) -> int:
        sum_,  coeff= 0, 26
        for char in s:
            sum_ *= coeff
            sum_ += ord(char)-64
        return sum_