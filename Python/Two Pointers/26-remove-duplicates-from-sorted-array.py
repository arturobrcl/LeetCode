class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1

        while r < len(nums):
            if nums[l] == nums[r]:
                try:
                    while nums[l] == nums[r]:
                        nums.pop(r)
                except:
                    break
            elif nums[l] != nums[r]:
                l += 1
                r += 1
