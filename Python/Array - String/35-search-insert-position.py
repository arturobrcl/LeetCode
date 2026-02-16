class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            is_there = True
        else: is_there = False
        if is_there == True:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            if target < nums[0]:
                return 0
            elif target > nums[len(nums) - 1]:
                return len(nums)
            for i in range(len(nums)):
                if i <= len(nums) - 2:
                    if nums[i] < target and nums[i+1] > target:
                        print(nums[i], nums[i+1])
                        return i + 1
            
