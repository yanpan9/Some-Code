from typing import List

class Solution_DFS:
    def letterCombinations(self, digits: str) -> List[str]:
        result = list()
        if not digits:
            return list()
        num2char = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        
        def dfs(lst, digits):
            if not digits:
                result.append(lst[:])
            else:
                for char in num2char[int(digits[0])]:
                    lst.append(char)
                    dfs(lst, digits[1:])
                    lst.pop()
        dfs([], digits)
        return ["".join(l) for l in result]

class Solution_BFS:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return list()
        digit_to_letter = {"2":"abc",
                           "3":"def",
                           "4":"ghi",
                           "5":"jkl",
                           "6":"mno",
                           "7":"pqrs",
                           "8":"tuv",
                           "9":"wxyz"}
        result = [""]
        for digit in digits:
            result = [s1+s2 for s1 in result for s2 in digit_to_letter[digit]]
        return result