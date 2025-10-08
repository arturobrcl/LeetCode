class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if not s:
            return True
        if not t:
            return False
        for i in range(len(t)):
            if s[j] == t[i]:
                j += 1
            if i == len(t) - 1 and j < len(s):
                return False
            if j == len(s):
                return True
