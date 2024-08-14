from typing import List, Tuple

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result: List[int] = asteroids
        i: int = 1
        while -1 < i < len(result):
            if result[i-1] * result[i] > 0:
                i += 1
            else:
                if result[i-1] < result[i]:
                    i += 1
                else:
                    if abs(result[i-1]) < abs(result[i]):
                        result.pop(i-1)
                        i -= 1
                    elif abs(result[i-1]) == abs(result[i]):
                        result.pop(i-1)
                        result.pop(i-1)
                        i -= 1
                    else:
                        result.pop(i)
        return result

    

sol: Solution = Solution()
asteroids: List[int] = [1,-2,-2,1]
print(sol.asteroidCollision(asteroids))