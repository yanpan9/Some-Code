class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        idx = length - 1
        res = 0
        while idx >= 0 and s[idx]==" ":
            idx -= 1
        while idx >= 0 and s[idx]!=" ":
            idx -=1
            res += 1
        return res