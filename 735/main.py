from typing import List, Tuple

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result: List[int] = asteroids
        i: int = 0


        while i < len(result):
            if result[i] < 0:
                for j in range(i - 1 ,-1,-1):
                    if result[i] * result[j] > 0:
                        break
                    if abs(result[i]) > result[j]:
                        result.pop(j)
                        i -= 1
                    elif result[j] == abs(result[i]):
                        result.pop(i)
                        result.pop(j)
                        i -= 1
                        break
                    else:
                        result.pop(i)
                        i -= 1
                        break
            i += 1
        return result

sol: Solution = Solution()
asteroids: List[int] = [1,1,-1,-2]
print(sol.asteroidCollision(asteroids))
