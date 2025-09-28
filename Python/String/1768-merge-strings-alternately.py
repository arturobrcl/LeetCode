class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        lenMin = min(len(word1), len(word2))
        for i in range(lenMin):
            word3 = word3 + word1[i] + word2[i]

        try:
            word3 = word3 + word1[lenMin:]
        finally:
            word3 = word3 + word2[lenMin:]
        return word3
