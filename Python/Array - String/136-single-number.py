class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singles = []
        for i in range(len(nums)):
            if nums[i] not in singles:
                singles.append(nums[i])
                nums[i] = ''
        for j in range(len(singles)):
            if singles[j] not in nums:
                return singles[j]
