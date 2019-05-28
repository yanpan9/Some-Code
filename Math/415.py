class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len_1, len_2 = len(num1), len(num2)
        if len_1 != len_2:
            if len_1 > len_2:
                num2 = "0"*(len_1-len_2)+num2
            else:
                num1 = "0"*(len_2-len_1)+num1
        result = ["" for _ in range(max(len_1, len_2))]
        count = 0
        for i in range(max(len_1, len_2)-1, -1,-1):
            add_val = int(num1[i])+int(num2[i])+count
            count, val = divmod(add_val, 10)
            result[i]=str(val)
        if count:
            return str(count)+"".join(result)
        else:
            return "".join(result)