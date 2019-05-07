class Solution:
    def countAndSay(self, n: int) -> str:
        def read_sequence(s):
            res = ""
            cur, count = None, 0
            for char in s:
                if cur!=char:
                    if cur:
                        res += (str(count)+cur)
                    cur = char
                    count = 1
                else:
                    count += 1
            res += (str(count)+char)
            return res
        s = "1"
        if n == 1:
            return s
        else:
            for i in range(1,n):
                s = read_sequence(s)
            return s