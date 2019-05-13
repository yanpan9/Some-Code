class Solution:
    def romanToInt(self, s: str) -> int:
        char2num = {"I":1,
                    "IV":4,
                    "V":5, 
                    "IX":9, 
                    "X":10,
                    "XL":40,
                    "L":50,
                    "XC":90, 
                    "C":100, 
                    "CD":400,
                    "D":500,
                    "CM":900,
                    "M":1000}
        i, length = 0, len(s)
        res = 0
        while i < length:
            if s[i:i+2] in char2num:
                res += char2num[s[i:i+2]]
                i += 2
            else:
                res += char2num[s[i]]
                i += 1
        return res