class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        k = c = 0
        while k < len(g) and c < len(s):
            if s[c] >= g[k]:
                k += 1
                c += 1
            else:
                c += 1
        
        return k
