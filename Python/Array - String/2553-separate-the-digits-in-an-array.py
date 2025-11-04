class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for number in nums:
            answer += (list(map(int, str(number))))

        return answer
