class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        try:
            for i in range(100):
                letters = set([s[i] for s in strs])
                if len(letters)==1:
                    res+=letters.pop()
                else:
                    break
        except:
            return res
        return res