class Solution_Stack:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        left, right = "(", ")"
        max_len = 0
        for idx,char in enumerate(s):
            if char==left:
                stack.append(idx)
            else:
                last = stack.pop()
                if len(stack)==0:
                    stack.append(idx)
                else:
                    length = idx - stack[-1]
                    if length > max_len:
                        max_len = length
        return max_len

class Solution_DP:
    def longestValidParentheses(self, s: str) -> int:
        length = len(s)
        dp = [0]*(length+1)
        left, right = "(", ")"
        for idx,char in enumerate(s[1:], 1):
            if char == right:
                if s[idx-1]==left:
                    dp[idx+1]=dp[idx-1]+2
                elif dp[idx]!=0 and idx-dp[idx]>0 and s[idx-dp[idx]-1]==left:
                    dp[idx+1]=dp[idx]+2+dp[idx-dp[idx]-1]
        return max(dp)