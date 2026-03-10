class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_index = {num: i for i, num in enumerate(nums1)}
        n = len(nums1)
        result = [-1] * n
        stack = []
        
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                index = stack.pop()
                val = nums2[index]
                
                if val in num_to_index:
                    result[num_to_index[val]] = nums2[i]
            
            stack.append(i)
        
        return result
