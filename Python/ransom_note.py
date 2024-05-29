class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        len1 = len(ransomNote)
        len2 = len(magazine)
        i, j = 0, 0
        while i < len1 and j < len2:
            if ransomNote[i] == magazine[j]:
                ransomNote[i] = ''
                magazine[j] = ''
                i += 1
                j = 0
            else:
                j += 1
        print(ransomNote)
        if ransomNote == ['']*len1:
            return True
        else:
            return False
