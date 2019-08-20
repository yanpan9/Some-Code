class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        for ele in paths:
            if not ele or ele==".":
                continue
            elif ele=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(ele)
        return "/"+"/".join(stack)