from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for s in strs:
            number = self.str2int(s)
            if number in res:
                res[number].append(s)
            else:
                res[number] = [s]
        return list(res.values())
    def str2int(self, s: str) -> int:
        number, step = 0, 3
        for char in s:
            number += 1<<((ord(char)-97)*step)
        return number