from typing import List, Tuple

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        tmp:set = set(arr)
        cnt: List[int] = []

        for i in tmp:
            if arr.count(i) in cnt:
                return False
            else:
                cnt.append(arr.count(i))
        return True


arr: List[int] = [1,2]
sol: Solution = Solution()
print(sol.uniqueOccurrences(arr))