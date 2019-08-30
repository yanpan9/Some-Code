class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l = len(s)
        s2t = dict()
        t2s = dict()
        for i in range(l):
            if s[i] in s2t and t[i] in t2s:
                if s2t[s[i]]!=t[i] or t2s[t[i]]!=s[i]:
                    return False
            elif s[i] in s2t or t[i] in t2s:
                return False
            else:
                s2t[s[i]]=t[i]
                t2s[t[i]]=s[i]
        else:
            return True