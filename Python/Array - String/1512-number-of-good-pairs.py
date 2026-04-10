class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        l, r = 0, 1
        while r < len(nums):
            while l < r:
                if nums[l] == nums[r]:
                    pairs += 1
                l += 1
            r += 1
            l = 0
        return pairs
