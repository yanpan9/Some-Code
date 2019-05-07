class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        left_parentheses = {"(", "[", "{"}
        match_pattern = {")":"(",
                         "]":"[",
                         "}":"{"}
        for char in s:
            if char in left_parentheses:
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                else:
                    if stack.pop()!=match_pattern[char]:
                        return False
        if len(stack)==0:
            return True
        else:
            return False