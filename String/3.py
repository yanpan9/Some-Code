class Solution_Slidingwindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = i = j = 0
        char_set = set()
        length = len(s)
        while i<length and j<length:
            char = s[j]
            if char in char_set:
                char_set.remove(s[i])
                i += 1
            else:
                char_set.add(char)
                j += 1
                res = max(res, j-i)
        return res

class Solution_Slidingwindow2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = i = j = 0
        char_dict = dict()
        length = len(s)
        while i<length and j<length:
            char = s[j]
            if char in char_dict:
                i = max(i, char_dict[char]+1)
                char_dict[char] = j
                j += 1
            else:
                char_dict[char] = j
                j += 1
            res = max(res, j-i)
        return res