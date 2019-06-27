from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()
        def dfs(lst, n1, n2, n):
            if n2==n:
                res.append("".join(lst))
                #print(res[-1])
            else:
                if n1<n:
                    lst.append("(")
                    dfs(lst, n1+1, n2, n)
                    lst.pop()
                if n1>n2:
                    lst.append(")")
                    dfs(lst, n1, n2+1, n)
                    lst.pop()

        dfs(["("], 1, 0, n)
        return res
