class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for i in range(0, len(ransomNote)):
            if ransomNote[i] in magazine:
                ransomNote[i].pop()
                
