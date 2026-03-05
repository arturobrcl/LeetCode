class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tempmaxcon = 0
        maxcon = 0
        for n in nums:
            if n == 1:
                tempmaxcon += 1
                if tempmaxcon > maxcon:
                    maxcon = tempmaxcon
            elif n == 0:
                tempmaxcon = 0
        return maxcon 
