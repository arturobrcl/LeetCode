class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        damage = duration

        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] >= duration:
                damage += duration
            elif timeSeries[i+1] - timeSeries[i] < duration:
                damage += timeSeries[i+1] - timeSeries[i]

        return damage
