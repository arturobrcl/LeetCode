class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        n = len(nums)
        nums2 = [0] * n
        for i in range(n):
            nums2[i] = pre
            pre *= nums[i]

        for i in range(n-1, -1, -1):
            nums2[i] *= post
            post *= nums[i]

        return nums2
