class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = int(len(candyType)/2)
        stack = []
        i = 0
        for i in range(len(candyType)):
            if candyType[i] not in stack and len(stack) < n:
                stack.append(candyType[i])
            elif len(stack) == n:
                break

        return len(stack)
