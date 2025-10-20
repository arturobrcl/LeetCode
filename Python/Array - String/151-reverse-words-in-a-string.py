class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = [var for var in s if var]
        return " ".join(s[::-1])
