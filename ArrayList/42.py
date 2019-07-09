from typing import List

class Solution_Stack_1:
    # Ugly solution, break time limitation
    def trap(self, height: List[int]) -> int:
        stack = [(0, -1)]
        length = len(height)
        idx, res = 0, 0
        while idx<length:
            h = height[idx]
            if stack:
                pre = stack[-1]
                if h>=pre[0]:
                    for i in range(pre[0],h+1):
                        if stack and i == stack[-1][0]:
                            res += idx-stack[-1][1]-1
                            stack.pop()
                    stack.append((h, idx))
                else:
                    for i in range(pre[0]-1,h,-1):
                        stack.append((i, pre[-1]))
                    stack.append((h, idx))
            else:
                stack.append((h, idx))
            idx += 1
        return res

class Solution_Stack:
    def trap(self, height: List[int]) -> int:
        stack = list()
        length = len(height)
        idx, res = 0, 0
        while idx<length:
            while stack and height[idx]>height[stack[-1]]:
                pre = stack.pop()
                if stack:
                    h = min(height[idx], height[stack[-1]])-height[pre]
                    w = idx-stack[-1]-1
                    res += h*w
                else:
                    break
            stack.append(idx)
            idx += 1
        return res

class Solution_DoublePoint:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left,right = 0, length-1
        res = left_max = right_max = 0
        while left<right:
            if height[left]<height[right]:
                if height[left]>left_max:
                    left_max =  height[left]
                res += left_max-height[left]
                left += 1
            else:
                if height[right]>right_max:
                    right_max = height[right]
                res += right_max-height[right]
                right -= 1
        return res