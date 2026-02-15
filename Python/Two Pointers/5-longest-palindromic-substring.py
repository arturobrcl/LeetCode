class Solution:
    def longestPalindrome(self, s: str) -> str:
        center = 0
        longest = s[0]
        best_start, best_len = 0, 0
        if len(s) == 1:
            return s
        if s == s[::-1]:
            return s
        for center in range(len(s)):
            l, r = center, center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > best_len:
                    best_start, best_len = l, cur_len
                l -= 1
                r += 1
            
            l, r = center - 1, center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > best_len:
                    best_start, best_len = l, cur_len
                l -= 1
                r += 1

        return s[best_start:best_start + best_len]
