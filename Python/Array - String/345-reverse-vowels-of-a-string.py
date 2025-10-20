class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowelsInS = [letter for letter in s if letter in vowels]
        for i in range(len(s)):
            if s[i] in vowels:
                s = s[:i] + vowelsInS[-1] +s[i+1:]
                vowelsInS = vowelsInS[:-1]

        return s
