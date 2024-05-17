class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
      # Declaration of Variables
        i = m - 1
        j = n - 1
        k = m + n - 1

      # While there is a number in j compare the two biggest numbers left in the arrays of nums1 and nums2 
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]: # If the value in nums1 is bigger than the value in nums2 then write it in the original nums1
                nums1[k] = nums1[i]
                k -= 1
                i -=1
            else: # In any other case, replace the value of nums1 with the value of nums2
                nums1[k] = nums2[j] 
                k -= 1
                j -= 1
