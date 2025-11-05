class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numset = set(nums)
        maxim = 0
        n = 0
        for i in numset:
            count = 0
            for m in nums:
                if i == m:
                    count += 1
            if count > maxim:
                maxim = count
                n = i
        return n
