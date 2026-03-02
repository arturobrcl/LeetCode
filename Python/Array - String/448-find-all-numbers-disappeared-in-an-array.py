class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        complete = list(range(1, len(nums)+1))
        missing = list(set(complete) - set(nums))
        return missing 
