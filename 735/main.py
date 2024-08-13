from typing import List, Tuple

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result: List[int] = []
        if not asteroids:
            return []
        
        result.append(asteroids.pop())
        for planet in asteroids:
            tmp: int = asteroids.pop()
                
        return
    

sol: Solution = Solution()
asteroids: List[int] = [5,10,-5]
print(sol.asteroidCollision(asteroids))