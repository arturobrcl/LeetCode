class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Create a copy of nums to avoid changes in nums affecting nums2
        nums2 = nums.copy()
        
        n = len(nums)
        k = k % n  # Handle cases where k is greater than the length of the array
        
        for i in range(n):
            nums[(i + k) % n] = nums2[i]
