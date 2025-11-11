class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        
        for i in range(len(shortest)):
            prefix = shortest[:i + 1]
            for word in strs:
                if not word.startswith(prefix):
                    return shortest[:i]
        return shortest
