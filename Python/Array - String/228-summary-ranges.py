class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(2**31+1)
        temp = []
        ranges = []
        for i in range(len(nums) - 1):
            if abs(nums[i] - nums[i+1]) == 1:
                temp.append(nums[i])
            elif abs(nums[i] - nums[i+1]) > 1 and len(temp) > 0:
                temp.append(nums[i])
                ranges.append(str(temp[0]) + "->" + str(temp[-1]))
                temp = []
            elif abs(nums[i] - nums[i+1]) > 1 and not temp:
                temp.append(nums[i])
                ranges.append(str(temp[0]))
                temp = []      
        return ranges
