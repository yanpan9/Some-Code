from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = list()
        idx = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1]==popped[idx]:
                stack.pop()
                idx += 1
        return not bool(stack)