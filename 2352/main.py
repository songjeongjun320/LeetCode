from typing import List, Tuple

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt: int = 0
        for i in range(len(grid)):
            tmp: list[int] = []
            for j in range(len(grid)):
                tmp.append(grid[j][i])
            cnt += grid.count(tmp)
        return cnt
    
sol = Solution() 
grid: List[List[int]] = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(sol.equalPairs(grid))