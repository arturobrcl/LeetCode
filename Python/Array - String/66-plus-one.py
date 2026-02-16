class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int(''.join(map(str, digits)))
        return list(map(int, str(digits + 1)))
