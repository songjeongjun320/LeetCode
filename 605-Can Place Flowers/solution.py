from typing import List, Tuple

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:return True
        for i in range(0,len(flowerbed)):
            if n == 0: break
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i] == flowerbed[i - 1] == flowerbed[i + 1]:
                    flowerbed[i] = 1
                    n -= 1
        if n == 0:
            return True
        return False

solution = Solution()
flowerbed: List[int] = [1,0,0,0,1,0,0]
n: int = 2
print(solution.canPlaceFlowers(flowerbed, n))
