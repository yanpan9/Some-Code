class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = [word for word in reversed(s.split(" ")) if word]
        return " ".join(words)