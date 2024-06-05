class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums.count(nums[i]) > 2:
                del nums[i]
