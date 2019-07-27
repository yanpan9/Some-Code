from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = list()
        m = len(words)
        if m:
            n = len(words[0])
            length = len(s)
            idx, sub_len = 0, m*n-1
            counter = dict()
            for word in words:
                counter[word]=counter.get(word, 0)+1
            while idx<length-sub_len:
                if s[idx:idx+n] in words:
                    t_words = counter.copy()
                    for i in range(m):
                        sub_str = s[(idx+i*n):(idx+(i+1)*n)]
                        if sub_str in t_words:
                            t_words[sub_str]-=1
                            if not t_words[sub_str]:
                                t_words.pop(sub_str)
                        else:
                            break
                    else:
                        res.append(idx)
                idx += 1
        return res