class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        hasGreatest = []
        for i in candies:
            if i + extraCandies >= max(candies):
                hasGreatest.append(True)
            else:
                hasGreatest.append(False)
        return hasGreatest
