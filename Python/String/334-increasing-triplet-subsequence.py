class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = 0 
        if len(set(nums)) < 3:
            return False
        while i < len(nums) - 2:
            for sec in range(i + 1, len(nums)):
                if nums[sec] > nums[i]:
                    j = sec
                    if any(y > nums[j] for y in nums[j+1::]):
                        return True
            i += 1

        return False    
                
