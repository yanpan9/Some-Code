from collections import Counter
from collections import deque

class Solution:
    def isValid(self, pattern, count):
        for key in pattern:
            if key in count:
                if count[key]>=pattern[key]:
                    continue
                else:
                    return False
            else:
                return False
        else:
            return True
    
    def minWindow(self, s: str, t: str) -> str:
        la, ans = 2**31-1, ""
        ls = len(s)
        if ls:
            counter = Counter(t)
            left = right = 0
            swd = dict()
            queue = deque()
            while right<ls:
                c = s[right]
                if c in counter:
                    swd[c] = swd.get(c, 0)+1
                    queue.append((c, right))
                    right += 1
                    if self.isValid(counter, swd):
                        while True:
                            char, idx = queue[0]
                            if swd[char]-1>=counter[char]:
                                left = idx+1
                                swd[char] -= 1
                                queue.popleft()
                            else:
                                left = idx
                                break
                        if right-left<la:
                            la = right-left
                            ans = s[left:right]
                else:
                    right += 1
            return ans
        else:
            return ans