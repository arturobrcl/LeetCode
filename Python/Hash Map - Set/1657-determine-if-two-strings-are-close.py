class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        setWord1, setWord2 = sorted(set(word1)), sorted(set(word2))
        mp1 = {}
        mp2 = {}
        if setWord1 != setWord2:
            return False
        elif len(word1) != len(word2):
            return False
        for letter in word1:
            mp1[letter] = mp1.get(letter, 0) + 1
        for letter in word2:
            mp2[letter] = mp2.get(letter, 0) + 1

        if sorted(mp1.values()) == sorted(mp2.values()):
            return True
        else:
            return False
