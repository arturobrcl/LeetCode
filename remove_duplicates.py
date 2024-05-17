class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in nums[:i]:
                del nums[i]
                k -= 1
