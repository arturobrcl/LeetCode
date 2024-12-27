class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted([ch for ch in s])
        t = sorted([ch for ch in t])
        if s == t:
            return True
        else:
            return False
