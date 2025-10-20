class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = "aeiou"
        maxCount = 0
        for i in range(len(s)-k+1):
            count = sum(list(map(s[i:(i+k)].count, v)))
            if count > maxCount:
                maxCount = count
        return maxCount
