from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = [word for word in reversed(s.split(" ")) if word]
        return " ".join(words)

class Solution_My:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        l = len(s)
        st, ed = 0, l-1
        while st< l and s[st]==" ":
            st += 1
        while ed>0 and s[ed]==" ":
            ed -= 1
        ed += 1
        if st>=ed:
            return ""
        s = s[st:ed]
        l = ed-st
        st = ed = 0
        queue = deque()
        while ed<l:
            while ed<l and s[ed]!=" ":
                ed += 1
            queue.appendleft(s[st:ed])
            while ed<l and s[ed]==" ":
                ed += 1
            st = ed
        return " ".join(queue)