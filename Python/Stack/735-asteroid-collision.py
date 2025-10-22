class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remaining = []
        for a in asteroids:
            if not remaining or a > 0:
                remaining.append(a)
            elif a < 0 and remaining[-1] < 0:
                remaining.append(a)
            while remaining and a < 0 and remaining[-1] > 0:
                diff = a + remaining[-1]
                if diff < 0:
                    remaining.pop(-1)
                    if not remaining or remaining[-1] < 0:
                        remaining.append(a)
                elif diff > 0:
                    break
                elif diff == 0:
                    remaining.pop()
                    break       
            
        return remaining
