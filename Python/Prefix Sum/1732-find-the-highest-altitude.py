class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        max = -inf
        for i in range(len(gain)):
            sum += gain[i]
            if sum > max:
                max = sum

        return max if max > 0 else 0
