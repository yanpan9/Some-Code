class Solution:
    def intToRoman(self, num: int) -> str:
        char2num = {"I":1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000}
        high2low = {"V":"I",
                    "X":"I",
                    "L":"X",
                    "C":"X",
                    "D":"C",
                    "M":"C"}
        chars = ["M", "D", "C", "L", "X", "V", "I"]
        res = list()
        for char in chars:
            while num>=char2num[char]:
                res.append(char)
                num-=char2num[char]
            if num==0:
                break
            if num>=char2num[char]-char2num[high2low[char]]:
                num = num-char2num[char]+char2num[high2low[char]]
                res.append(high2low[char])
                res.append(char)
        return "".join(res)