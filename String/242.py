class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.str2int(s)==self.str2int(t)
    
    def str2int(self, s: str) -> int:
        number, step = 0, 3
        for char in s:
            number += 1<<((ord(char)-97)*step)
        return number