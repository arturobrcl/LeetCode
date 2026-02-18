class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        complete = list(range(len(nums)+1))
        for i in range(len(complete)):
            if complete[i] not in nums:
                return complete[i]
