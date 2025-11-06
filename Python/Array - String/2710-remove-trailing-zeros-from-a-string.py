class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i in range(len(num)):
            if int(num[-1]) > 0:
                return num
            if int(num[-i-1]) > 0:
                return num[:-i]
