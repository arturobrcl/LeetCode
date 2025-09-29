class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shortest = str1 if len(str1) <= len(str2) else str2

        for i in range(len(shortest), 0, -1):
            pattern = shortest[:i]

            if len(str1) % i != 0 or len(str2) % i != 0:
                continue

            if pattern * (len(str1) // i) == str1 and pattern * (len(str2) // i) == str2:
                return pattern

        return ""
