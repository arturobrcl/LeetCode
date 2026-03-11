class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstr = list("qwertyuiop")
        secondr = list("asdfghjkl")
        thirdr = list("zxcvbnm")
        result = []
        for word in words:
            if set(list(word.lower())).issubset(firstr):
                result.append(word)
            elif set(list(word.lower())).issubset(secondr):
                result.append(word)
            elif set(list(word.lower())).issubset(thirdr):
                result.append(word)

        return result
