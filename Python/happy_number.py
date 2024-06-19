class Solution:
    def isHappy(self, n: int) -> bool:
        indicator = 0
        max_iterations=10
        iteration_count = 0
        while indicator != 1:
            nlist = [int(x) for x in str(n)]
            total = 0
            for num in nlist:
                total += num**2
            indicator = total
            n = total
            iteration_count += 1
            if iteration_count > max_iterations:
                return False
        return True
