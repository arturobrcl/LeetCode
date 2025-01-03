class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        expected = None
        i,j = 0,1
        while expected != target:
            expected = nums[i] + nums[j]
            if expected != target:
                j += 1
                if j == len(nums):
                    i += 1
                    j = i + 1
            else:
                return [i, j]
