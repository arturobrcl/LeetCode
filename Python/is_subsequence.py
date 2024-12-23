class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(0, len(s)):
            print(s[i])
            print(t)
            if s[i] in t:
                t = t.split(s[i],1)[1]
            else:
                return False
        return True
