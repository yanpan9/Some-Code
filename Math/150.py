import operator

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = {"+":operator.add,
                "-":operator.sub,
                "*":operator.mul,
                "/":lambda a,b:int(operator.truediv(a,b))}
        stack = list()
        for ele in tokens:
            if ele not in oper:
                stack.append(int(ele))
            else:
                b = stack.pop()
                a = stack.pop()
                res = oper[ele](a, b)
                stack.append(res)
        return int(stack.pop())
