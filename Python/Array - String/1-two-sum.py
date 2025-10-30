class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f, s = 0, 1
        sum = 0
        while f < len(nums) - 1:
            sum = nums[f] + nums[s]
            if sum == target:
                return [f, s]
            elif sum != target:
                s += 1
            if s == len(nums):
                f += 1
                s = f + 1
