from typing import List

class Solution_Bruteforce:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        len_h, len_n = len(haystack), len(needle)
        for i in range(len_h-len_n+1):
            if haystack[i:i+len_n]==needle:
                return i
        return -1 

class Solution_KMP:
    def strStr(self, haystack: str, needle: str) -> int:
        array = self.calNextArray(needle)
        len_1, len_2 = len(haystack), len(needle)
        i = j = 0
        while i<len_1 and j<len_2:
            if j==-1 or haystack[i]==needle[j]:
                i+=1; j+=1
            else:
                j = array[j]
        if j==len_2:
            return i - len_2
        else:
            return -1
        
    def calNextArray(self, pattern: str) -> List[int]:
        length = len(pattern)
        array = [-1 for _ in range(length)]
        i, j = 0 ,-1
        while i < length-1:
            if j==-1 or pattern[i]==pattern[j]:
                i += 1
                j += 1
                array[i]=j
            else:
                j = array[j]
        return array