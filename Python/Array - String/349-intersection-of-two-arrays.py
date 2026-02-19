class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        maxlen = max(len(nums1), len(nums2))
        for i in range(maxlen):
            if i < len(nums1):
                if nums1[i] in nums1 and nums1[i] in nums2:
                    intersect.append(nums1[i])
            if i < len(nums2):
                if nums2[i] in nums1 and nums2[i] in nums2:
                    intersect.append(nums2[i])
        
        return list(set(intersect))
