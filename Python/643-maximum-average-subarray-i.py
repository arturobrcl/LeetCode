class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        maxAvg = windowSum/k
        for i in range(k, len(nums)):
            windowSum += nums[i] - nums[i-k]
            if windowSum/k > maxAvg:
                maxAvg = windowSum/k 

        return maxAvg
