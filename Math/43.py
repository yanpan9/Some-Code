class Solution_Normal:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        len_1, len_2 = len(num1), len(num2)
        result = [0 for _ in range(len_1+len_2)]
        for i,m in enumerate(num2[::-1]):
            for j,n in enumerate(num1[::-1]):
                result[i+j] += int(m)*int(n)
        quotient = 0
        for i in range(len_1+len_2):
            quotient, remainder = divmod(result[i]+quotient, 10)
            result[i] = remainder
        while True:
            if result[-1]==0:
                result.pop()
            else:
                break
        result = [str(i) for i in result[::-1]]
        return "".join(result)