class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)
        if len_a==len_b:
            pass
        elif len_a > len_b:
            b = "0"*(len_a-len_b)+b
        else:
            a = "0"*(len_b-len_a)+a
        count, result = 0, [0 for _ in range(max(len_a, len_b))]
        for i in range(max(len_a,len_b)-1, -1, -1):
            count, val = divmod(int(a[i])+int(b[i])+count, 2)
            result[i] = val
        if count:
            result.insert(0, count)
        result = [str(i) for i in result]
        return "".join(result)