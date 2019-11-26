class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        s = list(s)
        vowels = {"a","e", "i", "o", "u", "A", "E", "I", "O", "U"}
        while l<r:
            while l<r and s[l] not in vowels:
                l += 1
            while l<r and s[r] not in vowels:
                r -= 1
            if l!=r:
                s[r], s[l] = s[l], s[r]
                l += 1
                r -= 1
        return "".join(s)