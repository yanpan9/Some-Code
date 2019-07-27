from typing import List

class Solution_BruteForce:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = list()
        m = len(words)
        if m:
            n = len(words[0])
            length = len(s)
            idx, sub_len = 0, m*n-1
            while idx<length-sub_len:
                if s[idx:idx+n] in words:
                    t_words = words[:]
                    for i in range(m):
                        sub_str = s[(idx+i*n):(idx+(i+1)*n)]
                        if sub_str in t_words:
                            t_words.remove(sub_str)
                        else:
                            break
                    else:
                        res.append(idx)
                idx += 1
        return res